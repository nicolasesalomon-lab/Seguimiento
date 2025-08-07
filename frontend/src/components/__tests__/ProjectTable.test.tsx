import { render, screen } from '@testing-library/react';
import ProjectTable, { Project } from '../ProjectTable';

test('renders project rows', () => {
  const data: Project[] = [
    { id: 1, modelo: 'PE-CT4205', producto: 'Prod', marca: 'Marca' },
  ];
  render(<ProjectTable projects={data} />);
  expect(screen.getByText('PE-CT4205')).toBeInTheDocument();
});
