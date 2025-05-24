# Farm Visit Project

## Deployment to Vercel

This Django project is configured for deployment on Vercel. Follow these steps to deploy:

### Prerequisites

1. A Vercel account (sign up at [vercel.com](https://vercel.com))
2. Vercel CLI installed (optional, for local testing)
3. Git installed on your machine

### Deployment Steps

1. **Push your code to a Git repository** (GitHub, GitLab, or Bitbucket)

2. **Connect your repository to Vercel**:

   - Go to [vercel.com](https://vercel.com) and sign in
   - Click "New Project"
   - Import your Git repository
   - Select the repository containing this project

3. **Configure the project**:

   - Vercel should automatically detect that this is a Django project
   - Set the following environment variables in the Vercel dashboard:
     - `DJANGO_SECRET_KEY`: A secure random string (keep this secret!)
     - `DATABASE_URL`: Your PostgreSQL database URL (Vercel provides this if you add a PostgreSQL integration)

4. **Deploy**:
   - Click "Deploy"
   - Vercel will build and deploy your application

### Local Development

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Run migrations:

   ```
   python farmproject/manage.py migrate
   ```

3. Start the development server:
   ```
   python farmproject/manage.py runserver
   ```

### Project Structure

- `farmproject/`: Main Django project directory
- `farmvisit/`: Django app for farm visit functionality
- `vercel.json`: Configuration for Vercel deployment
- `build_files.sh`: Build script for Vercel deployment
- `requirements.txt`: Python dependencies

### Notes

- Static files are served using WhiteNoise
- Media files are stored in the `media/` directory
- The project uses PostgreSQL on Vercel and SQLite for local development
