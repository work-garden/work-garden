"use client"
import { useState } from 'react';

export default function WhatsAppChat() {
  const [open, setOpen] = useState(false);
  
  return (
    <div style={{position:'fixed', bottom:'20px', right:'20px', zIndex:9999}}>
      {open && (
        <div style={{background:'white', padding:'15px', borderRadius:'12px', boxShadow:'0 4px 20px rgba(0,0,0,0.3)', marginBottom:'10px', width:'260px', color:'black'}}>
          <p style={{margin:'0 0 10px 0', fontWeight:'bold'}}>Garden Work 🌿</p>
          <a 
            href="https://wa.me/919999999999?text=Hi%20Garden%20Work"
            target="_blank"
            style={{background:'#25D366', color:'white', padding:'10px', borderRadius:'20px', display:'block', textAlign:'center', textDecoration:'none', fontWeight:'bold'}}
          >
            WhatsApp Chat
          </a>
        </div>
      )}
      <button 
        onClick={()=>setOpen(!open)}
        style={{background:'#25D366', border:'none', width:'60px', height:'60px', borderRadius:'50%', fontSize:'28px', cursor:'pointer'}}
      >
        💬
      </button>
    </div>
  );
}
