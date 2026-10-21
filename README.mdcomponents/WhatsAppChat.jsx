import { useState } from 'react';

export default function WhatsAppChat() {
  const [open, setOpen] = useState(false);
  const phoneNumber = "919999999999"; // ഇവിടെ നിന്റെ WhatsApp Number ഇടുക
  
  const message = "Hi! Garden Work-നെ കുറിച്ച് അറിയാൻ വേണ്ടിയാണ് 🌿";
  
  const openWhatsApp = () => {
    const url = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
  };

  return (
    <>
      {/* Floating Button */}
      <div style={{
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        zIndex: 9999
      }}>
        {open && (
          <div style={{
            background: 'white',
            padding: '15px',
            borderRadius: '10px',
            boxShadow: '0 4px 20px rgba(0,0,0,0.2)',
            marginBottom: '10px',
            width: '280px'
          }}>
            <h4 style={{margin: '0 0 10px 0'}}>Garden Work 🌿</h4>
            <p style={{fontSize: '14px', margin: '0 0 10px 0'}}>ഹായ്! എന്ത് സഹായം വേണം?</p>
            <button 
              onClick={openWhatsApp}
              style={{
                background: '#25D366',
                color: 'white',
                border: 'none',
                padding: '10px 20px',
                borderRadius: '20px',
                width: '100%',
                cursor: 'pointer',
                fontWeight: 'bold'
              }}
            >
              WhatsApp-ൽ Chat ചെയ്യുക
            </button>
          </div>
        )}
        
        <button 
          onClick={() => setOpen(!open)}
          style={{
            background: '#25D366',
            border: 'none',
            width: '60px',
            height: '60px',
            borderRadius: '50%',
            fontSize: '30px',
            cursor: 'pointer',
            boxShadow: '0 4px 10px rgba(0,0,0,0.3)'
          }}
        >
          💬
        </button>
      </div>
    </>
  );
}
