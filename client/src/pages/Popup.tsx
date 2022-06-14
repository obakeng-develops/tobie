import React from 'react'

function Popup() {

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
        <div></div>
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