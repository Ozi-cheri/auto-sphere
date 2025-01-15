# Autosphere

Auto-Sphere is a modern, interactive platform designed to showcase articles about cars, provide user interactivity through upvotes, downvotes, and comments, and offer an engaging experience for both users and administrators.

# Table Of Contents


- [Product Objective](#product-objective)
- [Site Users Goals](#site-users-goals)
- [Site Owner's Goals](#site-owners-goals)
- [GitHub Project Board](#github-project-board)
- [User Experience](#user-experience)
- [Wireframes](#wireframes)
- [User Stories](#user-stories)
- [Site Structure](#site-structure)
- [Color Used](#color-used)
- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)

## Project Objective
The **AutoSphere** project is designed to provide users with both old and  latest automobile articles, featuring engaging content and a seamless user experience.

## Site Users' Goals

The AutoSphere platform is designed to meet the following goals for its users:

- **Read Automobile Articles**
Users can browse through a collection of well-written and informative articles about various topics related to cars, including:
The latest car models and their features.
Industry trends and news about the automobile world.
Maintenance tips and buying guides for car enthusiasts.
Articles are displayed in an easy-to-read format with images to enhance the reading experience.

- **Comment and Engage in Discussions**
Users can actively participate in discussions by adding comments to articles.
The commenting feature allows users to:
Share their opinions or feedback on specific articles.
Interact with other users' comments to encourage community discussions.
The speech bubble icon shows the number of comments, making it easy for users to find highly-discussed articles.

- **Vote on Articles and Comments** 
Users can express their agreement or disagreement with the content by:
**Upvoting**: Showing appreciation for articles or comments they find helpful or interesting.
**Downvoting**: Indicating disagreement or dissatisfaction with the content.
Voting helps highlight the most popular articles and comments, improving content discovery and engagement.

By offering these features, AutoSphere ensures an interactive and engaging experience for all users, fostering a vibrant community of car enthusiasts.

## Site Owner's Goals

The AutoSphere site owner aims to achieve the following objectives:

- **Attract More Users**:  
  By consistently publishing high-quality and engaging content about automobiles, the platform seeks to draw in car enthusiasts, industry professionals, and casual readers interested in cars.

- **Provide an Intuitive and Interactive Platform**:  
  AutoSphere is designed to offer a seamless and user-friendly experience, enabling users to explore content, participate in discussions, and easily navigate the site. Features such as responsive design and clear navigation bars contribute to this goal.

- **Facilitate User Engagement**:  
  Encouraging interaction is key to building a vibrant community. Through voting systems for articles and comments, as well as providing an easy way for users to comment on articles, the site fosters active discussions and a sense of participation.

These goals work collectively to establish AutoSphere as a go-to platform for automotive news, insights, and community engagement.

## GitHub Project Board

The **GitHub Project Board** is an essential tool used for organizing and managing the development workflow of the AutoSphere project. It allows the team to visualize tasks, track progress, and ensure all project objectives are met efficiently.

### Structure of the Project Board
The project board is divided into the following columns to represent the workflow:

1. **To Do**:  
   This column contains all tasks and features that need to be implemented. It includes user stories, bug fixes, and enhancements that are planned but not yet started.

2. **In Progress**:  
   Tasks that are actively being worked on by the team are moved to this column. This provides a clear view of what is currently being developed.


3. **Done**:  
   Once a task is reviewed, tested, and deployed, it is moved to this column to indicate completion.

### Key Features of the GitHub Project Board

- **Task Categorization**:  
  Each task is represented as a card, which includes a title, description, labels, and assignees. Labels such as `bug`, `feature`, `enhancement`, and `documentation` help categorize the cards for clarity.

- **Progress Tracking**:  
  Tasks are moved across columns as they progress through the development pipeline, providing a visual representation of the project's status.

- **Integration with Issues**:  
  GitHub Issues are linked directly to the project board. This ensures that all tasks, including bugs and new features, are tracked in one place.

- **Milestones**:  
  Milestones are used to group related tasks and track progress toward significant project goals. Each milestone represents a feature release or a development phase.

- **Collaboration**:  
  The board supports collaboration by allowing team members to comment on tasks, assign tasks to specific developers, and prioritize items using drag-and-drop functionality.

### Example Workflow

1. **Adding a Task**:  
   A new task, such as "Add user authentication feature," is created as a card in the `To Do` column with a detailed description, a label (e.g., `feature`), and an assignee.

2. **Task in Progress**:  
   When a developer starts working on the feature, they move the card to the `In Progress` column.


4. **Completion**:  
   After successful review and testing, the card is moved to the `Done` column, indicating that the task is complete.


   ## Database Schema

The **Auto-Sphere** project uses a relational database schema designed to store and manage data efficiently for articles, comments, and user interactions. Below is the detailed table structure of the schema:

### 1. `Article` Table
Stores all articles published on the platform.

| **Field Name**  | **Data Type**          | **Description**                            |
|------------------|------------------------|--------------------------------------------|
| `id`            | AutoField (Primary Key) | Unique identifier for each article.        |
| `title`         | CharField (max_length=200) | Title of the article.                     |
| `content`       | TextField              | Detailed content of the article.           |
| `image`         | ImageField             | Associated image for the article.          |
| `created_at`    | DateTimeField          | Timestamp when the article was created.    |
| `upvotes`       | PositiveIntegerField   | Number of upvotes the article has received. |
| `downvotes`     | PositiveIntegerField   | Number of downvotes the article has received. |


### 2. `Comment` Table
Stores all comments associated with articles.

| **Field Name**  | **Data Type**          | **Description**                            |
|------------------|------------------------|--------------------------------------------|
| `id`            | AutoField (Primary Key) | Unique identifier for each comment.        |
| `article`       | ForeignKey (to `Article`) | Links the comment to a specific article.   |
| `name`          | CharField (max_length=100) | Name of the user who commented.            |
| `text`          | TextField              | Content of the comment.                    |
| `created_at`    | DateTimeField          | Timestamp when the comment was created.    |


### 3. `User` Table *(Optional if using Django’s default user model)*
Manages user authentication and permissions.

| **Field Name**  | **Data Type**          | **Description**                            |
|------------------|------------------------|--------------------------------------------|
| `id`            | AutoField (Primary Key) | Unique identifier for each user.           |
| `username`      | CharField (max_length=150) | Username chosen by the user.               |
| `email`         | EmailField             | User's email address.                      |
| `password`      | CharField              | Encrypted password for authentication.     |

