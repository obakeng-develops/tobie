import React from 'react'

function Popup() {

  const imageStyle = {
    backgroundImage: 'url(/images/ryan-plomp.jpg)',
    backgroundSize: 'cover',
    backgroundPosition: 'center'
  }

  return (
    <div className='shadow-lg p-6 w-1/4 rounded-lg'>
      <div className='flex justify-between'>
        <label className='font-overpass font-bold'>Save Product</label>
        <div>
          <i>H</i>
          <i>P</i>
          <i>X</i>
        </div>
      </div>
      <div>
        <div style={imageStyle} className='h-64 rounded-md my-3'></div>
        <div className='flex flex-col font-overpass'>
          <label>Nike Air Max</label>
          <label>R475</label>
        </div>
        <div>
          <button className='bg-black font-overpass text-white p-2 rounded-md w-full my-3'>Save</button>
        </div>
      </div>
    </div>
  )
}

export default Popup