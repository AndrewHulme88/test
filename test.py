data = {"id":1,"title":"Random","description":"Null","client_id":3,"deadline":"2023-10-13 18:30:05","status":"Proposal","created_at":"2023-10-13T05:26:17.000000Z","updated_at":"2023-10-13T05:26:17.000000Z","user_projects":[{"id":1,"name":"Rosendo Pfannerstill III","email":"admin@mallow-tech.com","email_verified_at":null,"is_client":0,"address":null,"country":null,"phone_number":null,"profile_image":null,"created_at":"2023-10-13T05:15:47.000000Z","updated_at":"2023-10-13T05:15:47.000000Z","pivot":{"project_id":1,"user_id":1}},{"id":22,"name":"MukeshPrakash","email":"mukeshprakash87@gmail.com","email_verified_at":null,"is_client":0,"address":null,"country":null,"phone_number":null,"profile_image":null,"created_at":"2023-10-13T05:17:12.000000Z","updated_at":"2023-10-13T05:17:12.000000Z","pivot":{"project_id":1,"user_id":22}}]}

user_ids = [user_project['pivot']['user_id'] for user_project in data['user_projects']]

print(user_ids)
