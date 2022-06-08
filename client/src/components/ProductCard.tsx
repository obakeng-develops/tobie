import React from 'react'

function ProductCard() {
  return (
    <div className='rounded-md'>
        <img src='/images/ryan-plomp.jpg' className='h-64 w-full'/>
        <div className='flex flex-col my-4 space-y-2'>
            <label className='text-2xl'>Nike Airforce 1</label>
            <label className='text-2xl'>R499</label>
            <button className='bg-neutral-900 text-2xl p-1 rounded-md text-white'>Buy</button>
        </div>
    </div>
  )
}

export default ProductCard