import { render, screen } from '@testing-library/react';
import Article from './Article';

test("renders Whoops", () => {
  render(<Article />);
  const element = screen.getByText(/Whoops/i);
  expect(element).toBeInTheDocument();
});