# ICT-JOB
#### You can try the ICT JOB platform [enter through this link](https://job.ictacademy.uz)
Open source data links that we used:

- https://data.egov.uz/rus
- https://stat.uz 
- https://mehnat.uz/ru/pages/otkrytye-dannye 
- https://commonvoice.mozilla.org/en 
- https://minenergy.uz/ru/lists/category/27 
- https://uba.uz/ru/services/open_data/ 
- [Kaggle](https://www.kaggle.com/datasets/nodirjonmuxammadali/jobs-classification)
#


<!-- GETTING STARTED -->
## Getting Started

<!-- Yaproq is telegram bot to predict and analysis wheat crop and find probability of yellow rust on the crop. It can detect the level of disease and gives the treatment recommendations. And also can predict the rate of yellow rust by using Humadity, temperature and current disease level. -->



### Installation

This are the steps to install the project and environment

- Clone the repo
   ```sh
   git clone https://github.com/jaloliddin1006/ict-job.git
   ```
- Create virtual environment  and activate
   ```sh
   virtualenv venv && source venv/bin/activate
   ```

- Install requirements (it may take some time to install the required libraries)
   ```sh
   pip install -r requirements.txt
   ```

- Copy [.env.example](https://github.com/jaloliddin1006/ict-job/blob/main/.env.example)  to .env and change variables to yours
   ```sh
   cp .env.example .env
   ```
- Create and Save the database
    ```sh
    python manage.py makemigrations && python manage.py migrate
    ```
- Create super user
    ```sh
    python manage.py createsuperuser
    ```
- Run the project
    ```sh
    python manage.py runserver
    ```



<!-- USAGE EXAMPLES -->
## Usage
<!-- After you press the start button, there will be appear menu and you can choose one of them. You can check the disease and its level by sending the picture and also you can check the situation on the near farms and check the weather information. If there is any problem with the near farms or weather that might be cause to yellow rust, we will warn you and give recommendations. -->


#

# You can watch the video in here : [Video Link](https://drive.google.com/file/d/1o5vLT0GODdQGHL8FIgKSQ_dO0VyhggBH/view?usp=drivesdk)

### Or this watch:
<video src="video_2023-11-12_13-47-49.mp4" controls title="Title"></video>
#
See the [open issues](https://github.com/jaloliddin1006/ict-job.git/issues) for a full list of proposed features (and known issues).

## Contact
ICT-JOB team:

- 👨‍💻 [Jonibek Yorqulov](https://gitlab.com/stat.jonibek0727/)

- 👨‍💻 [Jaloliddin Mamatmusayev ](https://github.com/jaloliddin1006)

- 👨‍💻 [Husan Ibragimov ](https://gitlab.com/husanIbragimov)



Project Link: [https://github.com/jaloliddin1006/ict-job](https://github.com/jaloliddin1006/ict-job)