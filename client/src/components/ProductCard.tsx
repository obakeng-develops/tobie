import React from 'react'

function ProductCard() {
  return (
    <div className='rounded-md'>
        <img src='/images/ryan-plomp.jpg' className='h-64 w-64'/>
        <div className='flex flex-col my-4 space-y-2'>
            <label>Nike Airforce 1</label>
            <label>R499</label>
            <button className='bg-neutral-900 rounded-md text-white'>Buy</button>
        </div>
    </div>
  )
}

export default ProductCard