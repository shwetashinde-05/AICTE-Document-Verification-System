import React, { useState, useEffect } from 'react';
import { UserRole, Application } from './types';
import { apiService } from './services/api';

export const App: React.FC = () => {
  const [role, setRole] = useState<UserRole>('institution');
  const [applications, setApplications] = useState<Application[]>([]);
  const [activeAppId, setActiveAppId] = useState<string>('APP-2026-001');

  useEffect(() => {
    apiService.getApplications()
      .then(apps => {
        setApplications(apps);
        if (apps.length > 0) setActiveAppId(apps[0].id);
      })
      .catch(console.error);
  }, []);

  const activeApp = applications.find(a => a.id === activeAppId) || applications[0];

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans">
      <header className="bg-[#002147] text-white p-3 text-xs">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div className="font-bold">AICTE SIH26261 | AI-Powered Compliance Verification Prototype</div>
          <div className="flex gap-2 items-center">
            <span>Portal:</span>
            <select
              value={role}
              onChange={(e) => setRole(e.target.value as UserRole)}
              className="text-slate-900 px-2 py-1 rounded text-xs"
            >
              <option value="institution">College Portal</option>
              <option value="aicte_officer">AICTE Officer Portal</option>
              <option value="aicte_admin">AICTE Admin Portal</option>
            </select>
          </div>
        </div>
      </header>

      <main className="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6">
        <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
          <h1 className="text-xl font-bold text-slate-900">
            {role === 'institution' && 'Institution Portal — ABC Institute of Technology'}
            {role === 'aicte_officer' && 'AICTE Officer Scrutiny Portal'}
            {role === 'aicte_admin' && 'AICTE System Administrator Portal'}
          </h1>
          <p className="text-xs text-slate-500 mt-1">
            Active Application: {activeApp?.application_id || 'APP-DEMO-001'} • Status: {activeApp?.status || 'Active'}
          </p>
        </div>
      </main>
    </div>
  );
};

export default App;
