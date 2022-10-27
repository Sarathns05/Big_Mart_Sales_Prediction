# Sales Prediction for Big Mart Outlets

An end-end Machine Learning Project to learn Data Analytics and apply machine learning algorithms to predict the Salesfor Big Mart Outlets


Dataset Description
------------------------------------------------------

BigMart has collected sales data from the year 2013, for 1559 products across 10 stores in different cities. Where the dataset consists of 12 attributes like Item Fat, Item Type, Item MRP, Outlet Type, Item Visibility, Item Weight, Outlet Identifier, Outlet Size, Outlet Establishment Year, Outlet Location Type, Item Identifier and Item Outlet Sales. Out of these attributes response variable is the Item Outlet Sales attribute and remaining attributes are used as the predictor variables.

The data-set is also based on hypotheses of store level and product level. Where store level involves attributes like: city, population density, store capacity, location, etc and the product level hypotheses involves attributes like: brand, advertisement, promotional offer, etc.

* Item_Identifier : Unique product ID
* Item_Weight : Weight of product
* Item_Fat_Content : Whether the product is low fat or not
* Item_Visibility : The % of total display area of all products in a store allocated to the particular product
* Item_Type : The category to which the product belongs
* Item_MRP : Maximum Retail Price (list price) of the product
* Outlet_Identifier : Unique store ID
* Outlet_Establishment_Year : The year in which store was established
* Outlet_Size : The size of the store in terms of ground area covered
* Outlet_Location_Type : The type of city in which the store is located
* Outlet_Type : Whether the outlet is just a grocery store or some sort of supermarket
* Item_Outlet_Sales : Sales of the product in the particular store. This is the outcome variable to be predicted.



Technology and tools used
------------------------------------------------------------------------------------
 
 * Python
 * Numpy and Pandas for data cleaning
 * Sklearn for model building
 * Google colab as IDE
 * Python flask for http server
 * HTML/CSS for UI
 * Heroku for deployement


Overview
----------

#### STEP 1: Data Preparation and model building

In this step, explore the data, do the required pre-processing and tried various Machine Learning models

#### STEP 2: Building the app using Flask and HTML

Here, fetch the best-performing model from step 1 and build a web app using Flask and HTML.

#### STEP 3: Deploying the app using Heroku

In the end deploy the working app through Heroku for the world to use our product.
  


Model Deployment
--------------------

* The web application is built using python library -> Flask and Web Programming languages -> HTML, CSS
* The entire application is finally deployed on Heroku by adding - Procfile (informs Heroku that which application is to be run first), Requirements         (notifies Heroku about the libraries that needs to be installed before deploying or running our application)
* See the deployed application [here](https://big-mart-sales-pred.herokuapp.com/)

![1663308507582-01](https://user-images.githubusercontent.com/108679625/190569160-0c9c6871-34b9-488f-98ed-3418a062f555.jpeg)


![IMG_20220916_113738](https://user-images.githubusercontent.com/108679625/190569495-d83e3c4d-aba9-4b51-8ffc-22037b34d9cf.png)



