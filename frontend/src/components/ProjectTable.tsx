import { Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material';

export interface Project {
  id: number;
  modelo: string;
  producto?: string;
  marca?: string;
}

interface Props {
  projects: Project[];
}

export default function ProjectTable({ projects }: Props) {
  return (
    <Table size="small" aria-label="projects table">
      <TableHead>
        <TableRow>
          <TableCell>Modelo</TableCell>
          <TableCell>Producto</TableCell>
          <TableCell>Marca</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {projects.map((p) => (
          <TableRow key={p.id} hover>
            <TableCell>{p.modelo}</TableCell>
            <TableCell>{p.producto}</TableCell>
            <TableCell>{p.marca}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
