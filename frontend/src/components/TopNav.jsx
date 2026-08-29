import React from 'react';
import { Bell, Settings } from 'lucide-react';

/**
 * UtilityBar — desktop-only right-side controls (bell, settings, avatar).
 * Nav links are in the Sidebar. This component has NO navigation links.
 */
export default function TopNav() {
  return (
    <header className="utility-bar" style={styles.header}>
      <div style={styles.rightSection}>
        <button style={styles.iconButton} aria-label="Notifications">
          <Bell size={24} strokeWidth={2.2} />
        </button>
        <button style={styles.iconButton} aria-label="Settings">
          <Settings size={24} strokeWidth={2.2} />
        </button>
        <div style={styles.avatarWrapper}>
          <img
            src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&q=80&w=120&h=120"
            alt="Asha Devi Profile"
            style={styles.avatarImg}
          />
        </div>
      </div>
    </header>
  );
}

const styles = {
  header: {
    justifyContent: 'flex-end',
    alignItems: 'center',
    padding: '16px 32px',
    backgroundColor: 'var(--bg-color)',
    borderBottom: '1px solid var(--border-color)',
    position: 'sticky',
    top: 0,
    zIndex: 10,
  },
  rightSection: {
    display: 'flex',
    alignItems: 'center',
    gap: '18px',
  },
  iconButton: {
    color: 'var(--primary-green)',
    padding: '8px',
    borderRadius: '50%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    minWidth: '44px',
    minHeight: '44px',
  },
  avatarWrapper: {
    width: '44px',
    height: '44px',
    borderRadius: '50%',
    border: '2px solid var(--primary-green)',
    overflow: 'hidden',
    boxShadow: '0 2px 8px rgba(30,101,53,0.1)',
    cursor: 'pointer',
  },
  avatarImg: {
    width: '100%',
    height: '100%',
    objectFit: 'cover',
  },
};
