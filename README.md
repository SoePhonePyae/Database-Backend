# Backend API with Flask

Database Backend For GameRental Application

**Customer Database** → [GitHub Repo](https://github.com/Kusk24/DataBase-Term-Project)  
**Staff & Admin Database** → [GitHub Repo](https://github.com/Tommyzizii/GameRentalService_Admin_Staff)  

### **👤 Contributors**
- **Customer** → Win Yu Maung  
- **Staff** → Soe Phone Pyae  
- **Admin** → Thant Zin Min
  



1. Install the required packages using pip:
    - Flask
    - SQLAlchemy
   Alternatively, you can run `setup` script to install the packages using virtual environment.

3. If there is an error in `database.py`, create a `config.properties` file containing the following variables with your PostgreSQL configurations:
    - DB_USER 
    - DB_PASSWORD 
    - DB_HOST 
    - DB_PORT 
    - DB_NAME 


4. Ensure that you use the exact column names defined in your Python model when querying in Flask.
