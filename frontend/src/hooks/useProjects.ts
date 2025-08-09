import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { Project } from '../components/ProjectTable';

export function useProjects() {
  return useQuery<Project[]>(['projects'], async () => {
    const res = await axios.get('/api/projects/');
    return res.data;
  });
}
