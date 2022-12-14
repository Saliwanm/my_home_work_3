from models.models import Plant, Employee, Salon

while True:
    print("1. Add new Plant\n" +
          "2. Get all plants\n" +
          "3. Get Plant by Id\n" +
          "4. Add new Employee\n" +
          "5. Get all employees\n" +
          "6. Get Employee by Id\n" +
          "7. Add new Salon\n" +
          "8. Get all salons\n" +
          "9. Get Salon by Id\n" +
          "10. Get all employees which work in all plants\n" +
          "11. Get all employees which work in all salons\n"
          )
    flag = int(input('Choose menu item: '))
    if flag == 1:
        name = input('Plant name: ')
        location = input('Plant location: ')
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        id = int(input("Type Id to search: "))
        Plant.get_by_id(id)
    elif flag == 4:
        name = input('Employee name: ')
        object_id = input('Employee work_id: ')
        type_of_work = input('Where work employee?: ')
        employee = Employee(name, object_id, type_of_work)
        employee.save()
    elif flag == 5:
        Employee.get_all()
    elif flag == 6:
        id = int(input("Type Id to search: "))
        Employee.get_by_id(id)
    elif flag == 7:
        name = input('Salon name: ')
        address = input('Address: ')
        size = input('size: ')
        salon = Salon(name, address, size)
        salon.save()
    elif flag == 8:
        Salon.get_all()
    elif flag == 9:
        id = int(input("Type Id to search: "))
        Salon.get_by_id(id)
    elif flag == 10:
        temp = 'plant'
        Employee.get_all_employee_ps(temp)
    elif flag == 11:
        temp = 'salon'
        Employee.get_all_employee_ps(temp)
