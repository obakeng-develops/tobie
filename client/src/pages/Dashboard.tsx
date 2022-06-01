import React from 'react'

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
        <div>Yo</div>
    </div>
  )
}

export default Dashboard