export type UserRole = 'institution' | 'aicte_officer' | 'aicte_admin';

export interface User {
  username: string;
  role: UserRole;
  name: string;
  organization: string;
  institution_id?: string;
  email: string;
}

export interface CourseIntake {
  programme: string;
  level: string;
  course_name: string;
  affiliating_body: string;
  approved_intake: number;
}

export interface InstitutionalReference {
  institution_name: string;
  permanent_id: string;
  application_id: string;
  academic_year: string;
  address: string;
  affiliating_university: string;
  approval_status: string;
  issue_date: string;
  courses: CourseIntake[];
  is_synthetic: boolean;
}

export interface VerificationFinding {
  finding_id: string;
  rule_name: string;
  field_name: string;
  expected_value: any;
  extracted_value: any;
  status: 'Matched' | 'Mismatched' | 'Missing' | 'Expired' | 'Manual Review Required' | 'Pending';
  severity: 'Pass' | 'Warning' | 'Critical';
  document_ref: string;
  page_ref: number;
  explanation: string;
  recommended_action: string;
}

export interface DocumentRecord {
  id: string;
  filename: string;
  doc_type: string;
  sha256_hash: string;
  file_size_bytes: number;
  upload_timestamp: string;
  ocr_processed: boolean;
  is_duplicate: boolean;
  anomaly_flags: string[];
  extracted_metadata?: any;
}

export interface InfrastructureItem {
  id: string;
  category: string;
  title: string;
  required_specs: string;
  submitted_photos: string[];
  submitted_documents: string[];
  status: 'Compliant' | 'Deficiency Found' | 'Pending Review' | 'Refer for Inspection';
  officer_remark?: string;
  last_inspected?: string;
}

export interface ReviewerAction {
  action_id: string;
  application_id: string;
  officer_name: string;
  officer_role: string;
  action_type: string;
  remarks: string;
  timestamp: string;
  related_finding_id?: string;
}

export interface Application {
  id: string;
  application_id: string;
  institution_id: string;
  institution_name: string;
  permanent_id: string;
  academic_year: string;
  category: string;
  status: string;
  created_at: string;
  submitted_at?: string;
  documents: DocumentRecord[];
  findings: VerificationFinding[];
  infrastructure_items: InfrastructureItem[];
  reviewer_actions: ReviewerAction[];
  overall_score: number;
}
