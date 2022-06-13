import Layout from '../components/Layout'
import Listings from '../components/Listings'
import CssBaseline from '@mui/material/CssBaseline'
import { createTheme, ThemeProvider } from '@mui/material'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
})

export default function IndexPage() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Layout title="MarketPlace Scraper">
        <Listings />
      </Layout>
    </ThemeProvider>
  )
}
