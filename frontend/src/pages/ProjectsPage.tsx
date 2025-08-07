import { Typography } from '@mui/material';
import ProjectTable from '../components/ProjectTable';
import { useProjects } from '../hooks/useProjects';
import { t } from '../i18n';

export default function ProjectsPage() {
  const { data, isLoading } = useProjects();
  return (
    <>
      <Typography variant="h4" gutterBottom>
        {t('projects')}
      </Typography>
      {isLoading ? t('loading') : <ProjectTable projects={data || []} />}
    </>
  );
}
