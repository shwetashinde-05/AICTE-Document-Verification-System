import { Application, InstitutionalReference } from '../types';

const API_BASE = '/api';

export const apiService = {
  async getApplications(): Promise<Application[]> {
    const res = await fetch(`${API_BASE}/applications`);
    const data = await res.json();
    return data.data;
  },

  async getApplicationById(id: string): Promise<Application> {
    const res = await fetch(`${API_BASE}/applications/${id}`);
    const data = await res.json();
    return data.data;
  },

  async getReferenceRecord(): Promise<InstitutionalReference> {
    const res = await fetch(`${API_BASE}/admin/reference-record`);
    const data = await res.json();
    return data.data;
  },

  async runScenario(scenarioName: string): Promise<any> {
    const res = await fetch(`${API_BASE}/demo/run-scenario/${scenarioName}`, { method: 'POST' });
    return await res.json();
  },

  async verifyCertificate(certNumber: string, appId?: string): Promise<any> {
    const res = await fetch(`${API_BASE}/issuer/verify`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ cert_number: certNumber, application_id: appId })
    });
    return await res.json();
  },

  async submitOfficerAction(actionData: {
    application_id: string;
    officer_name: string;
    officer_role: string;
    action_type: string;
    remarks: string;
  }): Promise<any> {
    const res = await fetch(`${API_BASE}/officer/action`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(actionData)
    });
    return await res.json();
  }
};
