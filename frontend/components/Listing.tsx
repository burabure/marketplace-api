import { Button, Card, CardActionArea, CardContent, CardHeader, CardMedia } from '@mui/material'
import React from 'react'
import CloseIcon from '@mui/icons-material/Close'
import { Listing as ListingType } from '../interfaces'

type Props = Pick<ListingType, 'id' | 'title' | 'price' | 'primaryPhotoUrl' | 'sellerLocation'>

export default function Listing({ id, title, price, primaryPhotoUrl, sellerLocation }: Props) {
  const subheader = `${price} - ${sellerLocation}`
  const openListing = () => {
    window.open(`https://www.facebook.com/marketplace/item/${id}`, '_blank')
  }
  return (
    <Card sx={{ maxWidth: 260, position: 'relative', paddingBottom: '80px' }}>
      <CardActionArea onClick={openListing}>
        <CardMedia component="img" width="260" image={primaryPhotoUrl} />
      </CardActionArea>
      <CardHeader title={title} {...{ subheader }} />
      <CardContent sx={{ position: 'absolute', bottom: 0, right: 0, left: 0 }}>
        <Button
          variant="outlined"
          color="secondary"
          startIcon={<CloseIcon />}
          sx={{ width: '100%' }}
        >
          Dismiss
        </Button>
      </CardContent>
    </Card>
  )
}
