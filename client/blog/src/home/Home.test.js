import { render, screen } from '@testing-library/react';
import App from './Home';

test("renders Joseph Smith's programming exercise", () => {
  render(<App />);
  const element = screen.getByText(/Joseph Smith's programming exercise/i);
  expect(element).toBeInTheDocument();
});
