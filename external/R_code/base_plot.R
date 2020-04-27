library(dplyr)
library(tidyverse)
library(lubridate)
library(ggplot2)
library(ggmap)
library(sf)
options(warn=-1)
conn <- src_mysql(dbname = "", 
                  host = "127.0.0.1", 
                  port = 3307, 
                  user = "",
                  password = "xxxxxxx")
conn2 <- src_mysql(dbname = "", 
                  host = "127.0.0.1", 
                  port = 3308, 
                  user = "",
                  password = "xxxxxxxx")
to_epoch <- function(v) {
  as_datetime(v) %>% as.integer() * 1000  
}
d <- function(v) {
  message(v)
  v
}
# 
tvh <- tbl(conn, 'A')


s <- as_datetime('2019-02-13 00:00:00')
e <- as_datetime('2019-02-14 00:00:00')
r <- tbl(conn2, 'ride')
rr <- r %>% filter()
rr_n <- rr %>% summarise(n = n()) %>% show()
rr_collected <- rr %>% collect() 
tracks <- function(Id) {
  x <- r %>% filter(id == Id) %>% 
    select(vehicle_id, created_at, cancelled_at, dropped_off_at) %>% collect()
  s <- to_epoch(x$created_at)
  e <- to_epoch(x$dropped_off_at)
  tvh %>% filter(vehicle_id == x$vehicle_id & (time_ms > s) & (time_ms < e)) %>% mutate(p = sql('ST_asText(location)')) %>%  collect()
}



# ride 240개를 골라서 
sampled_ride_ids <- sample(rr_collected$id, 240)
single_plot <- function(Id) {
  t <- tracks(d(Id)) 
  cex <- 1
  st_as_sfc(t$p, crs=4326) %>% plot(pch='+', cex=cex, sub=Id); 
}

# pdf에 전부 plot 한다
pdf("x.pdf", width=8*2, height=11*2)
par(mfrow=c(2,2))
i <- 0
for ( in ) {
  message(i)
  single_plot(Id)
  if (i == 4) {
    i <- 0
    next
  }
  i <- i + 1
} 
dev.off()