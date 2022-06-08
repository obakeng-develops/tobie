import React from 'react'

function ProductCard() {
  return (
    <div className='rounded-lg shadow-lg relative'>
        <img src='/images/ryan-plomp.jpg' className='h-64 w-full rounded-t-lg'/>
        <label className='absolute top-2 right-2 text-base bg-white p-2 rounded-md'>25% off</label>
        <div className='flex flex-col my-2 space-y-2 p-3'>
            <label className='text-xl'>Nike Airforce 1</label>
            <label className='text-xl'>R499</label>
            <button className='bg-neutral-900 text-xl p-1 rounded-md text-white'>Buy</button>
        </div>
    </div>
  )
}

export default ProductCard