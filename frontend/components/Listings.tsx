import { useEffect, useState } from 'react'
import Listing from './Listing'

export default function Listings() {
  const [listings, setListings] = useState(null)

  useEffect(() => {
    fetch('http://localhost:5000/listings')
      .then((response) => response.json())
      .then((json) => {
        setListings(json.listings)
      })
  }, [])

  if (listings === null) {
    return <p>No Listings</p>
  }

  return listings.map(({ id, title, price, primaryPhotoUrl, sellerLocation, seenAt }) => (
    <Listing
      {...{ id }}
      {...{ title }}
      {...{ price }}
      {...{ primaryPhotoUrl }}
      {...{ sellerLocation }}
      {...{ seenAt }}
    />
  ))
}
