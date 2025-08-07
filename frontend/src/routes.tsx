import { RouteObject } from 'react-router-dom';
import ProjectsPage from './pages/ProjectsPage';

const routes: RouteObject[] = [
  { path: '/', element: <ProjectsPage /> },
];

export default routes;
