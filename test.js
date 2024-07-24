const data = {
  "id": 1,
  "title": "Random",
  "user_projects": [
    {
      "id": 1,
      "pivot": {
        "user_id": 1
      }
    },
    {
      "id": 22,
      "pivot": {
        "user_id": 22
      }
    }
  ]
};

// Loop through the user_projects array and log each user_id
for (const user_project of data.user_projects) {
  console.log(user_project.pivot.user_id);
}
