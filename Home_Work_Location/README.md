## Introduction
From Twitter Data to Home & Work Location.


## Descriptive Data
```python
hour4home = range(22,24,1) + range(0,3,1) + range(6,9,1)
weekday4home = ['Tuesday', 'Wednesday', 'Thursday', 'Monday']
```

```
# of Tweets: 117719
% of Tweets: 24.85%
# of Users: 31337
% of Users: 45.35%
```

```python
hour4work = range(12,17)
weekday4work = ['Tuesday', 'Wednesday', 'Thursday', 'Monday', 'Friday']
```
```
# of Tweets: 51119
% of Tweets: 10.79%
# of Users: 18113
% of Users: 26.21%
```



##Notes
***Centroid*** or ***Gaussian Mixture:*** 
return Gaussian Mixture result, at least sent 4 tweets, else return centroid directly

***inner join*** [home.innerJoin(work)] or ***home-work left join*** [home.leftJoin(work)]:

```
home 31337
work 18113

inner_join
inner 9326

home & work: leftjoin
home_leftjoin 31337
```



## Output

| File                         | Note                                  | Type      |
| ---------------------------- | ------------------------------------- | --------- |
| **userLoc_Work.p**           | key=username; val=list of coordinates | dict      |
| **userLoc_Home.p**           | key=username; val=list of coordinates | dict      |
| **home_work_inner_join.csv** | Hx, Hy, Wx, Wy                        | DataFrame |
| **home_work_inner_join.p**   | Hx, Hy, Wx, Wy                        | DataFrame |
| **home_work_left_join.csv**  | Hx, Hy, Wx, Wy                        | DataFrame |
| **home_work_left_join.cp**   | Hx, Hy, Wx, Wy                        | DataFrame |

* *home_work_inner_join is recommended.*



## Next

* Use **Home Location** (in home_work_\*.csv) to *Spatial Join* **L Train Buffer Area (Brooklyn Part)** to find out **list of Target Users**.
* Only keep records (rows) of those Target Users in **home_work_\*** DataFrame.
* **Twitter Dat**a (mentioned above) and **LDHE data** Spatial Join **Community** (.shp), and output two Origin(Home)-Destination(Work) Matrix (**OD matrix**).
* **Normalization** by *col* *(Home)*
* **Test**
* Interpretation and Visualization
* Limitation and on-going work (Twitter API)
* Future Work



