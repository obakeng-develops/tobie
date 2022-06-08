import React from 'react'
import ProductCard from '../components/ProductCard'

function Dashboard() {
  return (
    <div className='flex'>
        <div className='top-0 bg-slate-800 h-screen w-64 text-white p-6 flex flex-col items-center space-y-16'>
            <img src='/images/tobie-logo.png' className='w-20 h-20'/>
            <div>
                <ul className='space-y-4'>
                    <li className='text-2xl font-overpass'>Saves</li>
                    <li className='text-2xl font-overpass'>Profile</li>
                    <li className='text-2xl font-overpass'>Settings</li>
                </ul>
            </div>
        </div>
        <div className='p-10 w-full'>
            <div className='my-8'>
                <input type='text' placeholder='Search' className='w-full bg-slate-200 p-3 rounded-md'/>
                <select className='p-2 border border-slate-800 rounded-md my-3'>
                    <option>Superbalist</option>
                    <option>Takealot</option>
                    <option>OneDayOnly</option>
                </select>
                <div className='my-5 font-overpass text-3xl grid grid-cols-4'>
                    <ProductCard/>
                </div>
            </div>
        </div>
    </div>
  )
}

export default Dashboard