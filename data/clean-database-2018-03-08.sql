--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.3
-- Dumped by pg_dump version 9.6.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = survey, pg_catalog;

ALTER TABLE ONLY survey.classifiertypeselector DROP CONSTRAINT surveyfk_fkey;
ALTER TABLE ONLY survey.classifiertype DROP CONSTRAINT classifiertypeselectorfk_fkey;
SET search_path = sample, pg_catalog;

ALTER TABLE ONLY sample.sampleunit DROP CONSTRAINT statefk_fkey;
ALTER TABLE ONLY sample.samplesummary DROP CONSTRAINT statefk_fkey;
ALTER TABLE ONLY sample.sampleunit DROP CONSTRAINT samplesummary_fkey;
ALTER TABLE ONLY sample.report DROP CONSTRAINT reporttypefk_fkey;
SET search_path = ras_ci, pg_catalog;

ALTER TABLE ONLY ras_ci.seft_instrument DROP CONSTRAINT seft_instrument_instrument_id_fkey;
ALTER TABLE ONLY ras_ci.instrument DROP CONSTRAINT instrument_survey_id_fkey;
ALTER TABLE ONLY ras_ci.instrument_exercise DROP CONSTRAINT instrument_exercise_instrument_id_fkey;
ALTER TABLE ONLY ras_ci.instrument_exercise DROP CONSTRAINT instrument_exercise_exercise_id_fkey;
ALTER TABLE ONLY ras_ci.instrument_business DROP CONSTRAINT instrument_business_instrument_id_fkey;
ALTER TABLE ONLY ras_ci.instrument_business DROP CONSTRAINT instrument_business_business_id_fkey;
SET search_path = public, pg_catalog;

ALTER TABLE ONLY public.tokens_oauthaccesstoken DROP CONSTRAINT tokens_refresh_token_id_73966741_fk_tokens_oauthrefreshtoken_id;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode DROP CONSTRAINT tokens_oauthauthor_user_id_4921b0a3_fk_credentials_oauthuser_id;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode_scopes DROP CONSTRAINT tokens_oauthauth_oauthscope_id_fa96eff3_fk_tokens_oauthscope_id;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode DROP CONSTRAINT tokens_oauthau_client_id_a3a1bf9a_fk_credentials_oauthclient_id;
ALTER TABLE ONLY public.tokens_oauthaccesstoken DROP CONSTRAINT tokens_oauthaccess_user_id_e5dc07c6_fk_credentials_oauthuser_id;
ALTER TABLE ONLY public.tokens_oauthaccesstoken_scopes DROP CONSTRAINT tokens_oauthacce_oauthscope_id_75cbc0c6_fk_tokens_oauthscope_id;
ALTER TABLE ONLY public.tokens_oauthaccesstoken DROP CONSTRAINT tokens_oauthac_client_id_0b06e756_fk_credentials_oauthclient_id;
ALTER TABLE ONLY public.tokens_oauthaccesstoken_scopes DROP CONSTRAINT toke_oauthaccesstoken_id_9f8ce9f3_fk_tokens_oauthaccesstoken_id;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode_scopes DROP CONSTRAINT e087e784de108b1bb0f263df6a6ee307;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_content_type_id_c4bce8eb_fk_django_content_type_id;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id;
SET search_path = partysvc, pg_catalog;

ALTER TABLE ONLY partysvc.pending_enrolment DROP CONSTRAINT pending_enrolment_respondent_id_fkey1;
ALTER TABLE ONLY partysvc.pending_enrolment DROP CONSTRAINT pending_enrolment_respondent_id_fkey;
ALTER TABLE ONLY partysvc.enrolment DROP CONSTRAINT enrolment_business_id_fkey;
ALTER TABLE ONLY partysvc.business_respondent DROP CONSTRAINT business_respondent_respondent_id_fkey;
ALTER TABLE ONLY partysvc.business_respondent DROP CONSTRAINT business_respondent_business_id_fkey;
ALTER TABLE ONLY partysvc.business_attributes DROP CONSTRAINT business_attributes_business_id_fkey;
SET search_path = collectionexercise, pg_catalog;

ALTER TABLE ONLY collectionexercise.sampleunitgroup DROP CONSTRAINT statefk_fkey;
ALTER TABLE ONLY collectionexercise.collectionexercise DROP CONSTRAINT statefk_fkey;
ALTER TABLE ONLY collectionexercise.sampleunit DROP CONSTRAINT sampleunittypefk_fkey;
ALTER TABLE ONLY collectionexercise.casetypeoverride DROP CONSTRAINT sampleunittypefk_fkey;
ALTER TABLE ONLY collectionexercise.casetypedefault DROP CONSTRAINT sampleunittype_fkey;
ALTER TABLE ONLY collectionexercise.sampleunit DROP CONSTRAINT sampleunitgroupfk_fkey;
ALTER TABLE ONLY collectionexercise.report DROP CONSTRAINT reporttypefk_fkey;
ALTER TABLE ONLY collectionexercise.sampleunitgroup DROP CONSTRAINT exercisefk_fkey;
ALTER TABLE ONLY collectionexercise.casetypeoverride DROP CONSTRAINT exercisefk_fkey;
ALTER TABLE ONLY collectionexercise.event DROP CONSTRAINT event_collexfk_fkey;
SET search_path = casesvc, pg_catalog;

ALTER TABLE ONLY casesvc."case" DROP CONSTRAINT state_fkey;
ALTER TABLE ONLY casesvc.report DROP CONSTRAINT reporttypefk_fkey;
ALTER TABLE ONLY casesvc.caseevent DROP CONSTRAINT category_fkey;
ALTER TABLE ONLY casesvc."case" DROP CONSTRAINT casegroup_fkey;
ALTER TABLE ONLY casesvc.response DROP CONSTRAINT case_fkey;
ALTER TABLE ONLY casesvc.caseevent DROP CONSTRAINT case_fkey;
SET search_path = actionexporter, pg_catalog;

ALTER TABLE ONLY actionexporter.templatemapping DROP CONSTRAINT templatenamefk_fkey;
ALTER TABLE ONLY actionexporter.actionrequest DROP CONSTRAINT sampleunitreffk_fkey;
ALTER TABLE ONLY actionexporter.report DROP CONSTRAINT reporttypefk_fkey;
ALTER TABLE ONLY actionexporter.actionrequest DROP CONSTRAINT contactfk_fkey;
SET search_path = action, pg_catalog;

ALTER TABLE ONLY action.report DROP CONSTRAINT reporttypefk_fkey;
ALTER TABLE ONLY action.actionrule DROP CONSTRAINT actiontypefk_fkey;
ALTER TABLE ONLY action.action DROP CONSTRAINT actiontypefk_fkey;
ALTER TABLE ONLY action.action DROP CONSTRAINT actionstatefk_fkey;
ALTER TABLE ONLY action.action DROP CONSTRAINT actionrulefk_fkey;
ALTER TABLE ONLY action.actionplanjob DROP CONSTRAINT actionplanjobstate_fkey;
ALTER TABLE ONLY action."case" DROP CONSTRAINT actionplanfk_fkey;
ALTER TABLE ONLY action.actionrule DROP CONSTRAINT actionplanfk_fkey;
ALTER TABLE ONLY action.action DROP CONSTRAINT actionplanfk_fkey;
ALTER TABLE ONLY action.actionplanjob DROP CONSTRAINT actionplanfk_fkey;
SET search_path = sample, pg_catalog;

DROP INDEX sample.sampleunit_statefk_index;
DROP INDEX sample.sampleunit_samplesummaryfk_index;
DROP INDEX sample.samplesummary_statefk_index;
SET search_path = ras_ci, pg_catalog;

DROP INDEX ras_ci.ix_survey_survey_id;
DROP INDEX ras_ci.ix_instrument_instrument_id;
DROP INDEX ras_ci.ix_exercise_exercise_id;
DROP INDEX ras_ci.ix_business_ru_ref;
SET search_path = public, pg_catalog;

DROP INDEX public.users_unique_key;
DROP INDEX public.user_perf_id;
DROP INDEX public.user_perf_email;
DROP INDEX public.user_identity_zone;
DROP INDEX public.tokens_oauthscope_scope_3bf35d98_like;
DROP INDEX public.tokens_oauthrefreshtoken_refresh_token_c8ea33b6_like;
DROP INDEX public.tokens_oauthauthorizationcode_scopes_9050429e;
DROP INDEX public.tokens_oauthauthorizationcode_scopes_6e643d1e;
DROP INDEX public.tokens_oauthauthorizationcode_e8701ad4;
DROP INDEX public.tokens_oauthauthorizationcode_code_36706cec_like;
DROP INDEX public.tokens_oauthauthorizationcode_2bfe9d72;
DROP INDEX public.tokens_oauthaccesstoken_scopes_713369b6;
DROP INDEX public.tokens_oauthaccesstoken_scopes_6e643d1e;
DROP INDEX public.tokens_oauthaccesstoken_e8701ad4;
DROP INDEX public.tokens_oauthaccesstoken_access_token_0ca96316_like;
DROP INDEX public.tokens_oauthaccesstoken_2bfe9d72;
DROP INDEX public.subdomain;
DROP INDEX public.sec_audit_principal_idx;
DROP INDEX public.sec_audit_created_idx;
DROP INDEX public.schema_version_s_idx;
DROP INDEX public.revocable_tokens_zone_id;
DROP INDEX public.oauth_code_uq_idx;
DROP INDEX public.oauth_code_expiresat_idx;
DROP INDEX public.key_in_zone;
DROP INDEX public.idx_revocable_token_user_id;
DROP INDEX public.idx_revocable_token_expires_at;
DROP INDEX public.idx_revocable_token_client_id;
DROP INDEX public.idx_mfa_unique_name;
DROP INDEX public.groups_unique_lower_key;
DROP INDEX public.groups_unique_key;
DROP INDEX public.group_membership_unique_key;
DROP INDEX public.group_membership_perf_idx;
DROP INDEX public.group_membership_perf_group_lower_idx;
DROP INDEX public.group_membership_perf_group_idx;
DROP INDEX public.external_group_unique_key;
DROP INDEX public.entity_in_zone;
DROP INDEX public.django_session_session_key_c0390e0f_like;
DROP INDEX public.django_session_de54fa62;
DROP INDEX public.django_admin_log_e8701ad4;
DROP INDEX public.django_admin_log_417f1b1c;
DROP INDEX public.credentials_oauthuser_email_3d9493c5_like;
DROP INDEX public.credentials_oauthclient_client_id_270ae079_like;
DROP INDEX public.auth_user_username_6821ab7c_like;
DROP INDEX public.auth_user_user_permissions_e8701ad4;
DROP INDEX public.auth_user_user_permissions_8373b171;
DROP INDEX public.auth_user_groups_e8701ad4;
DROP INDEX public.auth_user_groups_0e939a4f;
DROP INDEX public.auth_permission_417f1b1c;
DROP INDEX public.auth_group_permissions_8373b171;
DROP INDEX public.auth_group_permissions_0e939a4f;
DROP INDEX public.auth_group_name_a6ea08ec_like;
DROP INDEX public.audit_principal;
DROP INDEX public.audit_created;
SET search_path = notifygatewaysvc, pg_catalog;

DROP INDEX notifygatewaysvc.message_id_idx;
SET search_path = collectionexercise, pg_catalog;

DROP INDEX collectionexercise.sampleunitgroup_statefk_index;
DROP INDEX collectionexercise.sampleunitgroup_exercisefk_index;
DROP INDEX collectionexercise.sampleunit_sampleunittypefk_index;
DROP INDEX collectionexercise.sampleunit_sampleunitgroupfk_index;
DROP INDEX collectionexercise.cto_sampleunittypefk_index;
DROP INDEX collectionexercise.cto_exercisefk_index;
DROP INDEX collectionexercise.ctd_sampleunittypefk_index;
DROP INDEX collectionexercise.collectionexercise_statefk_index;
SET search_path = casesvc, pg_catalog;

DROP INDEX casesvc.response_casefk_index;
DROP INDEX casesvc.caseevent_categoryfk_index;
DROP INDEX casesvc.caseevent_casefk_index;
DROP INDEX casesvc.case_state_index;
DROP INDEX casesvc.case_casegroupfk_index;
SET search_path = actionexporter, pg_catalog;

DROP INDEX actionexporter.templatemapping_templatenamefk_index;
DROP INDEX actionexporter.actionrequest_sampleunitreffk_index;
DROP INDEX actionexporter.actionrequest_contactfk_index;
SET search_path = action, pg_catalog;

DROP INDEX action.case_actionplanfk_index;
DROP INDEX action.actiontype_name_index;
DROP INDEX action.actionrule_actiontypefk_index;
DROP INDEX action.actionrule_actionplanfk_index;
DROP INDEX action.actionplanjob_statefk_index;
DROP INDEX action.actionplanjob_actionplanfk_index;
DROP INDEX action.action_statefk_index;
DROP INDEX action.action_optlockversion_index;
DROP INDEX action.action_actiontypefk_index;
DROP INDEX action.action_actionrulefk_index;
DROP INDEX action.action_actionplanfk_index;
SET search_path = templatesvc, pg_catalog;

ALTER TABLE ONLY templatesvc.template DROP CONSTRAINT template_pkey;
ALTER TABLE ONLY templatesvc.classificationtype DROP CONSTRAINT classificationtype_pkey;
SET search_path = survey, pg_catalog;

ALTER TABLE ONLY survey.survey DROP CONSTRAINT survey_pkey;
ALTER TABLE ONLY survey.survey DROP CONSTRAINT survey_id_key;
ALTER TABLE ONLY survey.classifiertypeselector DROP CONSTRAINT classifiertypeselector_pkey;
ALTER TABLE ONLY survey.classifiertypeselector DROP CONSTRAINT classifiertypeselector_id_key;
ALTER TABLE ONLY survey.classifiertype DROP CONSTRAINT classifiertype_pkey;
SET search_path = sample, pg_catalog;

ALTER TABLE ONLY sample.sampleunitstate DROP CONSTRAINT sampleunitstate_pkey;
ALTER TABLE ONLY sample.sampleunit DROP CONSTRAINT sampleunit_uuid_key;
ALTER TABLE ONLY sample.sampleunit DROP CONSTRAINT sampleunit_pkey;
ALTER TABLE ONLY sample.samplesummarystate DROP CONSTRAINT samplesummarystate_pkey;
ALTER TABLE ONLY sample.samplesummary DROP CONSTRAINT samplesummary_uuid_key;
ALTER TABLE ONLY sample.samplesummary DROP CONSTRAINT samplesummary_pkey;
ALTER TABLE ONLY sample.reporttype DROP CONSTRAINT reporttype_pkey;
ALTER TABLE ONLY sample.report DROP CONSTRAINT report_uuid_key;
ALTER TABLE ONLY sample.report DROP CONSTRAINT report_pkey;
ALTER TABLE ONLY sample.databasechangeloglock DROP CONSTRAINT pk_databasechangeloglock;
ALTER TABLE ONLY sample.messagelog DROP CONSTRAINT messagelogpk_pkey;
ALTER TABLE ONLY sample.collectionexercisejob DROP CONSTRAINT collectionexercisejob_pkey;
SET search_path = ras_ci, pg_catalog;

ALTER TABLE ONLY ras_ci.survey DROP CONSTRAINT survey_pkey;
ALTER TABLE ONLY ras_ci.seft_instrument DROP CONSTRAINT seft_instrument_pkey;
ALTER TABLE ONLY ras_ci.instrument DROP CONSTRAINT instrument_pkey;
ALTER TABLE ONLY ras_ci.exercise DROP CONSTRAINT exercise_pkey;
ALTER TABLE ONLY ras_ci.business DROP CONSTRAINT business_pkey;
ALTER TABLE ONLY ras_ci.alembic_version DROP CONSTRAINT alembic_version_pkc;
SET search_path = public, pg_catalog;

ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
ALTER TABLE ONLY public.user_info DROP CONSTRAINT user_info_pkey;
ALTER TABLE ONLY public.user_google_mfa_credentials DROP CONSTRAINT user_google_mfa_credentials_pkey;
ALTER TABLE ONLY public.tokens_oauthscope DROP CONSTRAINT tokens_oauthscope_scope_key;
ALTER TABLE ONLY public.tokens_oauthscope DROP CONSTRAINT tokens_oauthscope_pkey;
ALTER TABLE ONLY public.tokens_oauthrefreshtoken DROP CONSTRAINT tokens_oauthrefreshtoken_refresh_token_key;
ALTER TABLE ONLY public.tokens_oauthrefreshtoken DROP CONSTRAINT tokens_oauthrefreshtoken_pkey;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode_scopes DROP CONSTRAINT tokens_oauthauthorizationcode_scopes_pkey;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode DROP CONSTRAINT tokens_oauthauthorizationcode_pkey;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode DROP CONSTRAINT tokens_oauthauthorizationcode_code_key;
ALTER TABLE ONLY public.tokens_oauthauthorizationcode_scopes DROP CONSTRAINT tokens_oauthauthorizati_oauthauthorizationcode_id_28200133_uniq;
ALTER TABLE ONLY public.tokens_oauthaccesstoken_scopes DROP CONSTRAINT tokens_oauthaccesstoken_scopes_pkey;
ALTER TABLE ONLY public.tokens_oauthaccesstoken_scopes DROP CONSTRAINT tokens_oauthaccesstoken_scope_oauthaccesstoken_id_1497353e_uniq;
ALTER TABLE ONLY public.tokens_oauthaccesstoken DROP CONSTRAINT tokens_oauthaccesstoken_refresh_token_id_key;
ALTER TABLE ONLY public.tokens_oauthaccesstoken DROP CONSTRAINT tokens_oauthaccesstoken_pkey;
ALTER TABLE ONLY public.tokens_oauthaccesstoken DROP CONSTRAINT tokens_oauthaccesstoken_access_token_key;
ALTER TABLE ONLY public.service_provider DROP CONSTRAINT service_provider_pkey;
ALTER TABLE ONLY public.schema_version DROP CONSTRAINT schema_version_pk;
ALTER TABLE ONLY public.revocable_tokens DROP CONSTRAINT revocable_tokens_pkey;
ALTER TABLE ONLY public.oauth_client_details DROP CONSTRAINT oauth_client_details_pkey;
ALTER TABLE ONLY public.authz_approvals DROP CONSTRAINT new_authz_approvals_pkey;
ALTER TABLE ONLY public.mfa_providers DROP CONSTRAINT mfa_providers_pkey;
ALTER TABLE ONLY public.identity_zone DROP CONSTRAINT identity_zone_pkey;
ALTER TABLE ONLY public.identity_provider DROP CONSTRAINT identity_provider_pkey;
ALTER TABLE ONLY public.groups DROP CONSTRAINT groups_pkey;
ALTER TABLE ONLY public.expiring_code_store DROP CONSTRAINT expiring_code_store_pkey;
ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_76bd3d3b_uniq;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
ALTER TABLE ONLY public.credentials_oauthuser DROP CONSTRAINT credentials_oauthuser_pkey;
ALTER TABLE ONLY public.credentials_oauthuser DROP CONSTRAINT credentials_oauthuser_email_key;
ALTER TABLE ONLY public.credentials_oauthclient DROP CONSTRAINT credentials_oauthclient_pkey;
ALTER TABLE ONLY public.credentials_oauthclient DROP CONSTRAINT credentials_oauthclient_client_id_key;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_14a6b632_uniq;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_94350c0c_uniq;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_01ab375a_uniq;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_0cd325b0_uniq;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
SET search_path = partysvc, pg_catalog;

ALTER TABLE ONLY partysvc.respondent DROP CONSTRAINT respondent_pkey;
ALTER TABLE ONLY partysvc.respondent DROP CONSTRAINT respondent_party_uuid_key;
ALTER TABLE ONLY partysvc.respondent DROP CONSTRAINT respondent_email_address_key;
ALTER TABLE ONLY partysvc.pending_enrolment DROP CONSTRAINT pending_enrolment_pkey;
ALTER TABLE ONLY partysvc.enrolment DROP CONSTRAINT enrolment_pkey;
ALTER TABLE ONLY partysvc.business_respondent DROP CONSTRAINT business_respondent_pkey;
ALTER TABLE ONLY partysvc.business DROP CONSTRAINT business_pkey;
ALTER TABLE ONLY partysvc.business DROP CONSTRAINT business_business_ref_key;
ALTER TABLE ONLY partysvc.business_attributes DROP CONSTRAINT business_attributes_pkey;
ALTER TABLE ONLY partysvc.alembic_version DROP CONSTRAINT alembic_version_pkc;
SET search_path = notifygatewaysvc, pg_catalog;

ALTER TABLE ONLY notifygatewaysvc.databasechangeloglock DROP CONSTRAINT pk_databasechangeloglock;
ALTER TABLE ONLY notifygatewaysvc.message DROP CONSTRAINT message_pkey;
SET search_path = iac, pg_catalog;

ALTER TABLE ONLY iac.databasechangeloglock DROP CONSTRAINT pk_databasechangeloglock;
ALTER TABLE ONLY iac.iac DROP CONSTRAINT code_pkey;
SET search_path = collectionexercise, pg_catalog;

ALTER TABLE ONLY collectionexercise.survey DROP CONSTRAINT surveypk_pkey;
ALTER TABLE ONLY collectionexercise.survey DROP CONSTRAINT survey_id_uuid_key;
ALTER TABLE ONLY collectionexercise.sampleunittype DROP CONSTRAINT sampleunittypepk_pkey;
ALTER TABLE ONLY collectionexercise.sampleunit DROP CONSTRAINT sampleunitpk_pkey;
ALTER TABLE ONLY collectionexercise.sampleunitgroup DROP CONSTRAINT sampleunitgrouppk_pkey;
ALTER TABLE ONLY collectionexercise.sampleunitgroupstate DROP CONSTRAINT sampleunitgroup_statepk_pkey;
ALTER TABLE ONLY collectionexercise.samplelink DROP CONSTRAINT samplelinkpk_pkey;
ALTER TABLE ONLY collectionexercise.reporttype DROP CONSTRAINT reporttype_pkey;
ALTER TABLE ONLY collectionexercise.report DROP CONSTRAINT report_uuid_key;
ALTER TABLE ONLY collectionexercise.report DROP CONSTRAINT report_pkey;
ALTER TABLE ONLY collectionexercise.databasechangeloglock DROP CONSTRAINT pk_databasechangeloglock;
ALTER TABLE ONLY collectionexercise.messagelog DROP CONSTRAINT messagelogpk_pkey;
ALTER TABLE ONLY collectionexercise.collectionexercise DROP CONSTRAINT exercisepk_pkey;
ALTER TABLE ONLY collectionexercise.event DROP CONSTRAINT event_pkey;
ALTER TABLE ONLY collectionexercise.event DROP CONSTRAINT event_id_key;
ALTER TABLE ONLY collectionexercise.event DROP CONSTRAINT event_collexfk_tag_key;
ALTER TABLE ONLY collectionexercise.collectionexercisestate DROP CONSTRAINT collectionexercise_statepk_pkey;
ALTER TABLE ONLY collectionexercise.collectionexercise DROP CONSTRAINT ce_id_uuid_key;
ALTER TABLE ONLY collectionexercise.casetypeoverride DROP CONSTRAINT casetypeoverridepk_pkey;
ALTER TABLE ONLY collectionexercise.casetypedefault DROP CONSTRAINT casetypedefaultpk_pkey;
SET search_path = casesvc, pg_catalog;

ALTER TABLE ONLY casesvc.casestate DROP CONSTRAINT state_pkey;
ALTER TABLE ONLY casesvc.response DROP CONSTRAINT response_pkey;
ALTER TABLE ONLY casesvc.reporttype DROP CONSTRAINT reporttype_pkey;
ALTER TABLE ONLY casesvc.report DROP CONSTRAINT report_uuid_key;
ALTER TABLE ONLY casesvc.report DROP CONSTRAINT report_pkey;
ALTER TABLE ONLY casesvc.databasechangeloglock DROP CONSTRAINT pk_databasechangeloglock;
ALTER TABLE ONLY casesvc.messagelog DROP CONSTRAINT messagelogpk_pkey;
ALTER TABLE ONLY casesvc.category DROP CONSTRAINT category_pkey;
ALTER TABLE ONLY casesvc.casegroup DROP CONSTRAINT casegroup_uuid_key;
ALTER TABLE ONLY casesvc.casegroup DROP CONSTRAINT casegroup_pkey;
ALTER TABLE ONLY casesvc.caseevent DROP CONSTRAINT caseevent_pkey;
ALTER TABLE ONLY casesvc."case" DROP CONSTRAINT case_uuid_key;
ALTER TABLE ONLY casesvc."case" DROP CONSTRAINT case_pkey;
SET search_path = actionexporter, pg_catalog;

ALTER TABLE ONLY actionexporter.template DROP CONSTRAINT templetenamepk_pkey;
ALTER TABLE ONLY actionexporter.address DROP CONSTRAINT sampleunitrefpk_pkey;
ALTER TABLE ONLY actionexporter.reporttype DROP CONSTRAINT reporttype_pkey;
ALTER TABLE ONLY actionexporter.report DROP CONSTRAINT report_uuid_key;
ALTER TABLE ONLY actionexporter.report DROP CONSTRAINT report_pkey;
ALTER TABLE ONLY actionexporter.databasechangeloglock DROP CONSTRAINT pk_databasechangeloglock;
ALTER TABLE ONLY actionexporter.messagelog DROP CONSTRAINT messagepk_pkey;
ALTER TABLE ONLY actionexporter.contact DROP CONSTRAINT contactpk_pkey;
ALTER TABLE ONLY actionexporter.templatemapping DROP CONSTRAINT actiontypenamepk_pkey;
ALTER TABLE ONLY actionexporter.actionrequest DROP CONSTRAINT actionrequestpk_pkey;
SET search_path = action, pg_catalog;

ALTER TABLE ONLY action.actionplanjobstate DROP CONSTRAINT statepk_pkey;
ALTER TABLE ONLY action.reporttype DROP CONSTRAINT reporttype_pkey;
ALTER TABLE ONLY action.report DROP CONSTRAINT report_uuid_key;
ALTER TABLE ONLY action.report DROP CONSTRAINT report_pkey;
ALTER TABLE ONLY action.databasechangeloglock DROP CONSTRAINT pk_databasechangeloglock;
ALTER TABLE ONLY action.outcomecategory DROP CONSTRAINT outcomecategory_pkey;
ALTER TABLE ONLY action.actionplan DROP CONSTRAINT name_key;
ALTER TABLE ONLY action.messagelog DROP CONSTRAINT messagepk_pkey;
ALTER TABLE ONLY action."case" DROP CONSTRAINT casepk_pkey;
ALTER TABLE ONLY action."case" DROP CONSTRAINT caseid_uuid_key;
ALTER TABLE ONLY action.actiontype DROP CONSTRAINT actiontypepk_pkey;
ALTER TABLE ONLY action.actionstate DROP CONSTRAINT actionstatepk_pkey;
ALTER TABLE ONLY action.actionrule DROP CONSTRAINT actionrulepk_pkey;
ALTER TABLE ONLY action.actionplan DROP CONSTRAINT actionplanpk_pkey;
ALTER TABLE ONLY action.actionplanjob DROP CONSTRAINT actionplanjobpk_pkey;
ALTER TABLE ONLY action.actionplanjob DROP CONSTRAINT actionplanjobid_uuid_key;
ALTER TABLE ONLY action.actionplan DROP CONSTRAINT actionplanid_uuid_key;
ALTER TABLE ONLY action.action DROP CONSTRAINT actionpk_pkey;
ALTER TABLE ONLY action.action DROP CONSTRAINT actionid_uuid_key;
SET search_path = templatesvc, pg_catalog;

SET search_path = survey, pg_catalog;

SET search_path = sample, pg_catalog;

SET search_path = ras_ci, pg_catalog;

SET search_path = public, pg_catalog;

SET search_path = partysvc, pg_catalog;

SET search_path = notifygatewaysvc, pg_catalog;

SET search_path = iac, pg_catalog;

SET search_path = collectionexercise, pg_catalog;

SET search_path = casesvc, pg_catalog;

SET search_path = actionexporter, pg_catalog;

SET search_path = action, pg_catalog;

SET search_path = survey, pg_catalog;

ALTER TABLE survey.survey ALTER COLUMN surveypk DROP DEFAULT;
ALTER TABLE survey.classifiertypeselector ALTER COLUMN classifiertypeselectorpk DROP DEFAULT;
ALTER TABLE survey.classifiertype ALTER COLUMN classifiertypepk DROP DEFAULT;
SET search_path = ras_ci, pg_catalog;

ALTER TABLE ras_ci.survey ALTER COLUMN id DROP DEFAULT;
ALTER TABLE ras_ci.seft_instrument ALTER COLUMN id DROP DEFAULT;
ALTER TABLE ras_ci.instrument ALTER COLUMN id DROP DEFAULT;
ALTER TABLE ras_ci.exercise ALTER COLUMN id DROP DEFAULT;
ALTER TABLE ras_ci.business ALTER COLUMN id DROP DEFAULT;
SET search_path = public, pg_catalog;

ALTER TABLE public.tokens_oauthscope ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tokens_oauthrefreshtoken ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tokens_oauthauthorizationcode_scopes ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tokens_oauthauthorizationcode ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tokens_oauthaccesstoken_scopes ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.tokens_oauthaccesstoken ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.credentials_oauthuser ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.credentials_oauthclient ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
SET search_path = partysvc, pg_catalog;

ALTER TABLE partysvc.respondent ALTER COLUMN id DROP DEFAULT;
ALTER TABLE partysvc.pending_enrolment ALTER COLUMN id DROP DEFAULT;
ALTER TABLE partysvc.business_attributes ALTER COLUMN id DROP DEFAULT;
SET search_path = templatesvc, pg_catalog;

DROP TABLE templatesvc.template;
DROP TABLE templatesvc.classificationtype;
SET search_path = survey, pg_catalog;

DROP SEQUENCE survey.survey_surveypk_seq;
DROP TABLE survey.survey;
DROP SEQUENCE survey.classifiertypeselector_classifiertypeselectorpk_seq;
DROP TABLE survey.classifiertypeselector;
DROP SEQUENCE survey.classifiertype_classifiertypepk_seq;
DROP TABLE survey.classifiertype;
SET search_path = sample, pg_catalog;

DROP TABLE sample.sampleunitstate;
DROP SEQUENCE sample.sampleunitseq;
DROP TABLE sample.sampleunit;
DROP TABLE sample.samplesummarystate;
DROP SEQUENCE sample.samplesummaryseq;
DROP TABLE sample.samplesummary;
DROP TABLE sample.reporttype;
DROP SEQUENCE sample.reportpkseq;
DROP TABLE sample.report;
DROP TABLE sample.messagelog;
DROP SEQUENCE sample.messagelogseq;
DROP TABLE sample.databasechangeloglock;
DROP TABLE sample.databasechangelog;
DROP SEQUENCE sample.collectionexercisejobseq;
DROP TABLE sample.collectionexercisejob;
SET search_path = ras_ci, pg_catalog;

DROP SEQUENCE ras_ci.survey_id_seq;
DROP TABLE ras_ci.survey;
DROP SEQUENCE ras_ci.seft_instrument_id_seq;
DROP TABLE ras_ci.seft_instrument;
DROP SEQUENCE ras_ci.instrument_id_seq;
DROP TABLE ras_ci.instrument_exercise;
DROP TABLE ras_ci.instrument_business;
DROP TABLE ras_ci.instrument;
DROP SEQUENCE ras_ci.exercise_id_seq;
DROP TABLE ras_ci.exercise;
DROP SEQUENCE ras_ci.business_id_seq;
DROP TABLE ras_ci.business;
DROP TABLE ras_ci.alembic_version;
SET search_path = public, pg_catalog;

DROP TABLE public.users;
DROP TABLE public.user_info;
DROP TABLE public.user_google_mfa_credentials;
DROP SEQUENCE public.tokens_oauthscope_id_seq;
DROP TABLE public.tokens_oauthscope;
DROP SEQUENCE public.tokens_oauthrefreshtoken_id_seq;
DROP TABLE public.tokens_oauthrefreshtoken;
DROP SEQUENCE public.tokens_oauthauthorizationcode_scopes_id_seq;
DROP TABLE public.tokens_oauthauthorizationcode_scopes;
DROP SEQUENCE public.tokens_oauthauthorizationcode_id_seq;
DROP TABLE public.tokens_oauthauthorizationcode;
DROP SEQUENCE public.tokens_oauthaccesstoken_scopes_id_seq;
DROP TABLE public.tokens_oauthaccesstoken_scopes;
DROP SEQUENCE public.tokens_oauthaccesstoken_id_seq;
DROP TABLE public.tokens_oauthaccesstoken;
DROP TABLE public.service_provider;
DROP TABLE public.sec_audit;
DROP TABLE public.schema_version;
DROP TABLE public.revocable_tokens;
DROP TABLE public.oauth_code;
DROP TABLE public.oauth_client_details;
DROP TABLE public.mfa_providers;
DROP TABLE public.identity_zone;
DROP TABLE public.identity_provider;
DROP TABLE public.groups;
DROP TABLE public.group_membership;
DROP TABLE public.external_group_mapping;
DROP TABLE public.expiring_code_store;
DROP TABLE public.django_session;
DROP SEQUENCE public.django_migrations_id_seq;
DROP TABLE public.django_migrations;
DROP SEQUENCE public.django_content_type_id_seq;
DROP TABLE public.django_content_type;
DROP SEQUENCE public.django_admin_log_id_seq;
DROP TABLE public.django_admin_log;
DROP SEQUENCE public.credentials_oauthuser_id_seq;
DROP TABLE public.credentials_oauthuser;
DROP SEQUENCE public.credentials_oauthclient_id_seq;
DROP TABLE public.credentials_oauthclient;
DROP TABLE public.authz_approvals;
DROP SEQUENCE public.auth_user_user_permissions_id_seq;
DROP TABLE public.auth_user_user_permissions;
DROP SEQUENCE public.auth_user_id_seq;
DROP SEQUENCE public.auth_user_groups_id_seq;
DROP TABLE public.auth_user_groups;
DROP TABLE public.auth_user;
DROP SEQUENCE public.auth_permission_id_seq;
DROP TABLE public.auth_permission;
DROP SEQUENCE public.auth_group_permissions_id_seq;
DROP TABLE public.auth_group_permissions;
DROP SEQUENCE public.auth_group_id_seq;
DROP TABLE public.auth_group;
SET search_path = partysvc, pg_catalog;

DROP SEQUENCE partysvc.respondent_id_seq;
DROP TABLE partysvc.respondent;
DROP SEQUENCE partysvc.pending_enrolment_id_seq;
DROP TABLE partysvc.pending_enrolment;
DROP TABLE partysvc.enrolment;
DROP TABLE partysvc.business_respondent;
DROP SEQUENCE partysvc.business_attributes_id_seq;
DROP TABLE partysvc.business_attributes;
DROP TABLE partysvc.business;
DROP TABLE partysvc.alembic_version;
SET search_path = notifygatewaysvc, pg_catalog;

DROP SEQUENCE notifygatewaysvc.messageseq;
DROP TABLE notifygatewaysvc.message;
DROP TABLE notifygatewaysvc.databasechangeloglock;
DROP TABLE notifygatewaysvc.databasechangelog;
SET search_path = iac, pg_catalog;

DROP TABLE iac.iac;
DROP TABLE iac.databasechangeloglock;
DROP TABLE iac.databasechangelog;
SET search_path = collectionexercise, pg_catalog;

DROP TABLE collectionexercise.survey;
DROP TABLE collectionexercise.sampleunittype;
DROP TABLE collectionexercise.sampleunitgroupstate;
DROP TABLE collectionexercise.sampleunitgroup;
DROP SEQUENCE collectionexercise.sampleunitgrouppkseq;
DROP TABLE collectionexercise.sampleunit;
DROP SEQUENCE collectionexercise.sampleunitpkseq;
DROP SEQUENCE collectionexercise.samplelinkpkseq;
DROP TABLE collectionexercise.samplelink;
DROP TABLE collectionexercise.reporttype;
DROP SEQUENCE collectionexercise.reportpkseq;
DROP TABLE collectionexercise.report;
DROP TABLE collectionexercise.messagelog;
DROP SEQUENCE collectionexercise.messagelogseq;
DROP SEQUENCE collectionexercise.eventpkseq;
DROP TABLE collectionexercise.event;
DROP TABLE collectionexercise.databasechangeloglock;
DROP TABLE collectionexercise.databasechangelog;
DROP TABLE collectionexercise.collectionexercisestate;
DROP TABLE collectionexercise.collectionexercise;
DROP SEQUENCE collectionexercise.exercisepkseq;
DROP TABLE collectionexercise.casetypeoverride;
DROP TABLE collectionexercise.casetypedefault;
SET search_path = casesvc, pg_catalog;

DROP SEQUENCE casesvc.responseseq;
DROP TABLE casesvc.response;
DROP TABLE casesvc.reporttype;
DROP SEQUENCE casesvc.reportpkseq;
DROP TABLE casesvc.report;
DROP TABLE casesvc.messagelog;
DROP SEQUENCE casesvc.messagelogseq;
DROP TABLE casesvc.databasechangeloglock;
DROP TABLE casesvc.databasechangelog;
DROP TABLE casesvc.category;
DROP TABLE casesvc.casestate;
DROP SEQUENCE casesvc.caseseq;
DROP SEQUENCE casesvc.casegroupstatusauditseq;
DROP TABLE casesvc.casegroupstatusaudit;
DROP SEQUENCE casesvc.casegroupseq;
DROP TABLE casesvc.casegroup;
DROP SEQUENCE casesvc.caseeventseq;
DROP TABLE casesvc.caseevent;
DROP TABLE casesvc."case";
DROP SEQUENCE casesvc.caserefseq;
SET search_path = actionexporter, pg_catalog;

DROP TABLE actionexporter.templatemapping;
DROP TABLE actionexporter.template;
DROP TABLE actionexporter.reporttype;
DROP SEQUENCE actionexporter.reportpkseq;
DROP TABLE actionexporter.report;
DROP TABLE actionexporter.messagelog;
DROP SEQUENCE actionexporter.messageseq;
DROP TABLE actionexporter.filerowcount;
DROP TABLE actionexporter.databasechangeloglock;
DROP TABLE actionexporter.databasechangelog;
DROP TABLE actionexporter.contact;
DROP SEQUENCE actionexporter.contactpkseq;
DROP TABLE actionexporter.address;
DROP SEQUENCE actionexporter.actionrequestpkseq;
DROP TABLE actionexporter.actionrequest;
SET search_path = action, pg_catalog;

DROP TABLE action.reporttype;
DROP SEQUENCE action.reportpkseq;
DROP TABLE action.report;
DROP TABLE action.outcomecategory;
DROP TABLE action.messagelog;
DROP SEQUENCE action.messageseq;
DROP TABLE action.databasechangeloglock;
DROP TABLE action.databasechangelog;
DROP SEQUENCE action.casepkseq;
DROP TABLE action."case";
DROP TABLE action.actiontype;
DROP TABLE action.actionstate;
DROP TABLE action.actionrule;
DROP TABLE action.actionplanjobstate;
DROP TABLE action.actionplanjob;
DROP SEQUENCE action.actionplanjobseq;
DROP TABLE action.actionplan;
DROP TABLE action.action;
DROP SEQUENCE action.actionpkseq;
SET search_path = sample, pg_catalog;

DROP FUNCTION sample.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text);
DROP FUNCTION sample.generate_sample_mi();
SET search_path = collectionexercise, pg_catalog;

DROP FUNCTION collectionexercise.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text);
DROP FUNCTION collectionexercise.generate_collectionexercise_mi();
SET search_path = casesvc, pg_catalog;

DROP FUNCTION casesvc.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text);
DROP FUNCTION casesvc.generate_response_chasing_report();
DROP FUNCTION casesvc.generate_case_events_report();
SET search_path = actionexporter, pg_catalog;

DROP FUNCTION actionexporter.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text);
DROP FUNCTION actionexporter.generate_print_volumes_mi();
SET search_path = action, pg_catalog;

DROP FUNCTION action.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text);
DROP FUNCTION action.generate_action_mi();
DROP FUNCTION action.createactions(p_actionplanjobpk integer);
SET search_path = public, pg_catalog;

DROP TYPE public.status;
DROP TYPE public.respondentstatus;
DROP TYPE public.kind;
DROP TYPE public.enrolmentstatus;
DROP TYPE public.communicationtype;
DROP TYPE public.businessrespondentstatus;
DROP EXTENSION pgcrypto;
DROP EXTENSION plpgsql;
DROP SCHEMA templatesvc;
DROP SCHEMA survey;
DROP SCHEMA sample;
DROP SCHEMA ras_ci;
DROP SCHEMA public;
DROP SCHEMA partysvc;
DROP SCHEMA notifygatewaysvc;
DROP SCHEMA iac;
DROP SCHEMA collectionexercise;
DROP SCHEMA casesvc;
DROP SCHEMA actionexporter;
DROP SCHEMA action;
--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: action; Type: SCHEMA; Schema: -; Owner: actionsvc
--

CREATE SCHEMA action;


ALTER SCHEMA action OWNER TO actionsvc;

--
-- Name: actionexporter; Type: SCHEMA; Schema: -; Owner: actionexportersvc
--

CREATE SCHEMA actionexporter;


ALTER SCHEMA actionexporter OWNER TO actionexportersvc;

--
-- Name: casesvc; Type: SCHEMA; Schema: -; Owner: casesvc
--

CREATE SCHEMA casesvc;


ALTER SCHEMA casesvc OWNER TO casesvc;

--
-- Name: collectionexercise; Type: SCHEMA; Schema: -; Owner: collectionexercisesvc
--

CREATE SCHEMA collectionexercise;


ALTER SCHEMA collectionexercise OWNER TO collectionexercisesvc;

--
-- Name: iac; Type: SCHEMA; Schema: -; Owner: iacsvc
--

CREATE SCHEMA iac;


ALTER SCHEMA iac OWNER TO iacsvc;

--
-- Name: notifygatewaysvc; Type: SCHEMA; Schema: -; Owner: notifygatewaysvc
--

CREATE SCHEMA notifygatewaysvc;


ALTER SCHEMA notifygatewaysvc OWNER TO notifygatewaysvc;

--
-- Name: partysvc; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA partysvc;


ALTER SCHEMA partysvc OWNER TO postgres;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: ras_ci; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA ras_ci;


ALTER SCHEMA ras_ci OWNER TO postgres;

--
-- Name: sample; Type: SCHEMA; Schema: -; Owner: samplesvc
--

CREATE SCHEMA sample;


ALTER SCHEMA sample OWNER TO samplesvc;

--
-- Name: survey; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA survey;


ALTER SCHEMA survey OWNER TO postgres;

--
-- Name: templatesvc; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA templatesvc;


ALTER SCHEMA templatesvc OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


SET search_path = public, pg_catalog;

--
-- Name: businessrespondentstatus; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE businessrespondentstatus AS ENUM (
    'ACTIVE',
    'INACTIVE',
    'SUSPENDED',
    'ENDED'
);


ALTER TYPE businessrespondentstatus OWNER TO postgres;

--
-- Name: communicationtype; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE communicationtype AS ENUM (
    'EMAIL',
    'LETTER',
    'SMS'
);


ALTER TYPE communicationtype OWNER TO postgres;

--
-- Name: enrolmentstatus; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE enrolmentstatus AS ENUM (
    'PENDING',
    'ENABLED',
    'DISABLED',
    'SUSPENDED'
);


ALTER TYPE enrolmentstatus OWNER TO postgres;

--
-- Name: kind; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE kind AS ENUM (
    'LEGAL_STATUS',
    'INDUSTRY',
    'SIZE',
    'GEOGRAPHY',
    'COLLECTION_EXERCISE',
    'RU_REF'
);


ALTER TYPE kind OWNER TO postgres;

--
-- Name: respondentstatus; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE respondentstatus AS ENUM (
    'CREATED',
    'ACTIVE',
    'SUSPENDED'
);


ALTER TYPE respondentstatus OWNER TO postgres;

--
-- Name: status; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE status AS ENUM (
    'uploading',
    'pending',
    'active'
);


ALTER TYPE status OWNER TO postgres;

SET search_path = action, pg_catalog;

--
-- Name: createactions(integer); Type: FUNCTION; Schema: action; Owner: actionsvc
--

CREATE FUNCTION createactions(p_actionplanjobpk integer) RETURNS boolean
    LANGUAGE plpgsql
    AS $$

DECLARE
v_text             text;
v_plan_name        text;
v_plan_description text;
v_errmess          text;
v_actionplanid     integer;
v_currentdatetime  timestamp;
v_number_of_rows   integer;

BEGIN

   SELECT j.actionplanFK FROM action.actionplanjob j WHERE j.actionplanjobPK = p_actionplanjobPK INTO v_actionplanid;

   v_currentdatetime := current_timestamp;
   --v_currentdatetime := '2016-09-09 01:00:01+01'; -- for testing


   v_number_of_rows := 0;

   -- Look at the case table to see if any cases are due to run for the actionplan passed in
   -- start date before or equal current date
   -- end date after or equal current date
   -- rules found, for plan passed in, due as days offset is less than or equal to days passed since start date (current date minus start date)
   IF EXISTS (SELECT 1
              FROM action.case c, action.actionrule r
              WHERE c.actionplanstartdate <= v_currentdatetime AND c.actionplanenddate >= v_currentdatetime
              AND r.daysoffset <= EXTRACT(DAY FROM (v_currentdatetime - c.actionplanstartdate))
              AND c.actionplanFk = v_actionplanid
              AND r.actionplanFK = c.actionplanFK) THEN

       -- Get plan description for messagelog using the actionplan passed in
      SELECT p.name, p.description
      FROM action.actionplan p
      WHERE p.actionplanPK = v_actionplanid INTO v_plan_name,v_plan_description;

      -- Collection Exercise start date reached, Run the rules due
      INSERT INTO action.action
        (
         id
        ,actionPK
        ,caseId
        ,caseFK
        ,actionplanFK
        ,actionruleFK
        ,actiontypeFK
        ,createdby
        ,manuallycreated
        ,situation
        ,stateFK
        ,createddatetime
        ,updateddatetime
        )
      SELECT
         gen_random_uuid()
        ,nextval('action.actionPKseq')
        ,l.id
        ,l.casePK
        ,l.actionplanFk
        ,l.actionrulePK
        ,l.actiontypeFK
        ,'SYSTEM'
        ,FALSE
        ,NULL
        ,'SUBMITTED'
        ,v_currentdatetime
        ,v_currentdatetime
       FROM
        (SELECT c.id
               ,c.casePK
               ,r.actionplanFK
               ,r.actionrulePK
               ,r.actiontypeFK
         FROM action.actionrule r
              ,action.case c
         WHERE  c.actionplanFk = v_actionplanid
         AND    r.actionplanFk = c.actionplanFK
         AND r.daysoffset <= EXTRACT(DAY FROM (v_currentdatetime - c.actionplanstartdate)) -- looking at start date to see if the rule is due
         AND c.actionplanstartdate <= v_currentdatetime AND c.actionplanenddate >= v_currentdatetime -- start date before or equal current date AND end date after or equal current date
         EXCEPT
         SELECT a.caseId
               ,a.caseFK
               ,a.actionplanFK
               ,a.actionruleFK
               ,a.actiontypeFK
         FROM action.action a
         WHERE a.actionplanFk = v_actionplanid) l;

      GET DIAGNOSTICS v_number_of_rows = ROW_COUNT; -- number of actions inserted

     IF v_number_of_rows > 0 THEN
         v_text := v_number_of_rows  || ' ACTIONS CREATED: ' || v_plan_description || ' (PLAN NAME: ' || v_plan_name || ') (PLAN ID: ' || v_actionplanid || ')';
         PERFORM action.logmessage(p_messagetext := v_text
                                  ,p_jobid := p_actionplanjobPK
                                  ,p_messagelevel := 'INFO'
                                  ,p_functionname := 'action.createactions');
      END IF;
   END IF;

   -- Update the date the actionplan was run on the actionplan table
   UPDATE action.actionplan
   SET lastrundatetime = v_currentdatetime
   WHERE actionplanPK  = v_actionplanid;

   -- Update the date the actionplan was run on the actionplanjob table
   UPDATE action.actionplanjob
   SET updateddatetime = v_currentdatetime
      ,stateFK = 'COMPLETED'
   WHERE actionplanjobPK =  p_actionplanjobPK
   AND   actionplanFK    =  v_actionplanid;

RETURN TRUE;

EXCEPTION

WHEN OTHERS THEN
    v_errmess := SQLSTATE;
    PERFORM action.logmessage(p_messagetext := 'CREATE ACTION(S) EXCEPTION TRIGGERED SQLERRM: ' || SQLERRM || ' SQLSTATE : ' || v_errmess
                             ,p_jobid := p_actionplanjobPK
                             ,p_messagelevel := 'FATAL'
                             ,p_functionname := 'action.createactions');
  RETURN FALSE;
END;

$$;


ALTER FUNCTION action.createactions(p_actionplanjobpk integer) OWNER TO actionsvc;

--
-- Name: generate_action_mi(); Type: FUNCTION; Schema: action; Owner: actionsvc
--

CREATE FUNCTION generate_action_mi() RETURNS boolean
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
DECLARE

v_contents      text;
r_dataline      record;
v_rows          integer;

BEGIN
    
    PERFORM action.logmessage(p_messagetext := 'GENERATING ACTION MI REPORT'
                              ,p_jobid := 0
                              ,p_messagelevel := 'INFO'
                              ,p_functionname := 'action.generate_action_mi');  
    
       v_rows     := 0;
       v_contents := '';
       v_contents := 'Action Plan No,Action Plan Name,Action Type,Action Plan Start Date,Days Offset,Handler,Count,State';

-- Action State Report

       FOR r_dataline IN (SELECT  template.actionplan                       AS actionplan
                                , template.plan_description                 AS action_plan_name
                                , template.type_description                 AS action_type
                                , action_case_cnt.actionplanstartdate::date AS action_plan_startdate      
                                , template.daysoffset                       AS daysoffset
                                , template.handler                          AS handler
                                , COALESCE(action_case_cnt.cnt,0) AS cnt
                                , action_case_cnt.actionstate     AS action_state     
                          FROM (SELECT COALESCE(cases.actionplanFK,actions.actionplanFK) AS  actionplan
                                     , cases.actionplanstartdate
                                     , actions.createddatetime
                                     , COALESCE(cases.actionrulePK,actions.actionruleFK) AS actionrule
                                     , COALESCE(cases.actiontypeFK,actions.actiontypeFK) AS actiontype
                                     , actions.stateFK                                   AS actionstate
                                     , COUNT(*) cnt
                                FROM (SELECT  c.actionplanFK
                                            , c.actionplanstartdate::DATE
                                            , c.casePK
                                            , r.actionrulePK
                                            , r.actiontypeFK
                                      FROM  action.case c
                                          , action.actionrule r
                                      WHERE c.actionplanFK = r.actionplanFK) cases
                                      FULL JOIN (SELECT a.actionplanFK
                                                      , a.createddatetime::DATE
                                                      , a.caseFK
                                                      , a.actionruleFK
                                                      , a.actiontypeFK
                                                      , a.stateFK
                                                 FROM action.action a) actions
                                      ON (actions.actionplanFK = cases.actionplanFK 
                                      AND actions.actionruleFK = cases.actionrulePK
                                      AND actions.actiontypeFK = cases.actiontypeFK
                                      AND actions.caseFK       = cases.casePK) 
                              GROUP BY actionplan, actionplanstartdate, actionrule, actiontype, actionstate, createddatetime) action_case_cnt 
                              FULL JOIN (SELECT  r.actionplanFK AS actionplan
                                               , r.actionrulePK AS actionrule
                                               , r.actiontypeFK AS actiontype
                                               , p.description  AS plan_description
                                               , t.description  AS type_description
                                               , r.daysoffset  
                                               , t.handler    
                                         FROM   action.actionplan p
                                              , action.actionrule r
                                              , action.actiontype t
                                         WHERE p.actionplanPK = r.actionplanFK 
                                         AND   r.actiontypeFK = t.actiontypePK) template
                                         ON (template.actionplan = action_case_cnt.actionplan 
                                         AND template.actiontype = action_case_cnt.actiontype
                                         AND template.actionrule = action_case_cnt.actionrule)
                                         ORDER BY template.actionplan,template.daysoffset,template.plan_description,action_plan_startdate) LOOP

                           v_contents := v_contents                         || CHR(10) 
                           || r_dataline.actionplan                         || ','
                           || r_dataline.action_plan_name                   || ','
                           || r_dataline.action_type                        || ','
                           || COALESCE(r_dataline.action_plan_startdate::text,'') || ','
                           || r_dataline.daysoffset                         || ','
                           || r_dataline.handler                            || ','
                           || r_dataline.cnt                                || ','
                           || COALESCE(r_dataline.action_state,'') ;   
             v_rows := v_rows+1;  
       END LOOP;       

       -- Insert the data into the report table
       INSERT INTO action.report (id, reportPK,reporttypeFK,contents, createddatetime) VALUES(gen_random_uuid(), nextval('action.reportPKseq'), 'ACTIONS', v_contents, CURRENT_TIMESTAMP); 

               
       PERFORM action.logmessage(p_messagetext := 'GENERATING ACTIONS MI REPORT COMPLETED ROWS WRIITEN = ' || v_rows
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'action.generate_action_mi'); 
      
    
       PERFORM action.logmessage(p_messagetext := 'ACTIONS MI REPORT GENERATED'
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'action.generate_action_mi');
      
  RETURN TRUE;

  EXCEPTION
  WHEN OTHERS THEN   
     PERFORM action.logmessage(p_messagetext := 'GENERATE REPORTS EXCEPTION TRIGGERED SQLERRM: ' || SQLERRM || ' SQLSTATE : ' || SQLSTATE
                               ,p_jobid := 0
                               ,p_messagelevel := 'FATAL'
                               ,p_functionname := 'action.generate_action_mi');
                               
  RETURN FALSE;
END;
$$;


ALTER FUNCTION action.generate_action_mi() OWNER TO actionsvc;

--
-- Name: logmessage(text, numeric, text, text); Type: FUNCTION; Schema: action; Owner: actionsvc
--

CREATE FUNCTION logmessage(p_messagetext text DEFAULT NULL::text, p_jobid numeric DEFAULT NULL::numeric, p_messagelevel text DEFAULT NULL::text, p_functionname text DEFAULT NULL::text) RETURNS boolean
    LANGUAGE plpgsql
    AS $$
DECLARE
v_text TEXT ;
v_function TEXT;
BEGIN
INSERT INTO action.messagelog
(messagetext, jobid, messagelevel, functionname, createddatetime )
values (p_messagetext, p_jobid, p_messagelevel, p_functionname, current_timestamp);
  RETURN TRUE;
EXCEPTION
WHEN OTHERS THEN
RETURN FALSE;
END;
$$;


ALTER FUNCTION action.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text) OWNER TO actionsvc;

SET search_path = actionexporter, pg_catalog;

--
-- Name: generate_print_volumes_mi(); Type: FUNCTION; Schema: actionexporter; Owner: actionexportersvc
--

CREATE FUNCTION generate_print_volumes_mi() RETURNS boolean
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
DECLARE

v_contents      text;
r_dataline      record;
v_rows          integer;

BEGIN
    
    PERFORM actionexporter.logmessage(p_messagetext := 'GENERATING PRINT VOLUMES MI REPORT'
                              ,p_jobid := 0
                              ,p_messagelevel := 'INFO'
                              ,p_functionname := 'actionexporter.generate_print_volumes_mi');  
    
       v_rows := 0;
       v_contents    := '';
       v_contents    := 'filename,rowcount,datesent,success'; -- Set header line    

       FOR r_dataline IN (SELECT * FROM actionexporter.filerowcount f WHERE NOT f.reported) LOOP
             v_contents := v_contents || chr(10) || r_dataline.filename || ',' || r_dataline.rowcount || ',' || r_dataline.datesent || ',' || r_dataline.sendresult;                                     
             v_rows := v_rows+1;  
             UPDATE actionexporter.filerowcount   
             SET reported = TRUE;
       END LOOP;       

       IF v_rows > 0 THEN  
          -- Insert the data into the report table
          INSERT INTO actionexporter.report(id, reportPK,reporttypeFK,contents, createddatetime) VALUES(gen_random_uuid(), nextval('actionexporter.reportPKseq'), 'PRINT_VOLUMES', v_contents, CURRENT_TIMESTAMP); 
       END IF;

       PERFORM actionexporter.logmessage(p_messagetext := 'GENERATING PRINT VOLUMES MI REPORT COMPLETED ROWS WRIITEN = ' || v_rows
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'actionexporter.generate_print_volumes_mi'); 
      
    
       PERFORM actionexporter.logmessage(p_messagetext := 'PRINT VOLUMES MI REPORT GENERATED'
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'actionexporter.generate_print_volumes_mi'); 
  RETURN TRUE;

  EXCEPTION
  WHEN OTHERS THEN   
     PERFORM actionexporter.logmessage(p_messagetext := 'GENERATE PRINT VOLUMES MI REPORT EXCEPTION TRIGGERED SQLERRM: ' || 

SQLERRM || ' SQLSTATE : ' || SQLSTATE
                               ,p_jobid := 0
                               ,p_messagelevel := 'FATAL'
                               ,p_functionname := 'actionexporter.generate_print_volumes_mi');
                               
  RETURN FALSE;
END;
$$;


ALTER FUNCTION actionexporter.generate_print_volumes_mi() OWNER TO actionexportersvc;

--
-- Name: logmessage(text, numeric, text, text); Type: FUNCTION; Schema: actionexporter; Owner: actionexportersvc
--

CREATE FUNCTION logmessage(p_messagetext text DEFAULT NULL::text, p_jobid numeric DEFAULT NULL::numeric, p_messagelevel text DEFAULT NULL::text, p_functionname text DEFAULT NULL::text) RETURNS boolean
    LANGUAGE plpgsql
    AS $$
DECLARE
v_text TEXT ;
v_function TEXT;
BEGIN

INSERT INTO actionexporter.messagelog (messagetext, jobid, messagelevel, functionname, createddatetime )
VALUES (p_messagetext, p_jobid, p_messagelevel, p_functionname, current_timestamp);

  RETURN TRUE;
EXCEPTION
WHEN OTHERS THEN
RETURN FALSE;
END;
$$;


ALTER FUNCTION actionexporter.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text) OWNER TO actionexportersvc;

SET search_path = casesvc, pg_catalog;

--
-- Name: generate_case_events_report(); Type: FUNCTION; Schema: casesvc; Owner: casesvc
--

CREATE FUNCTION generate_case_events_report() RETURNS boolean
    LANGUAGE plpgsql
    AS $$
DECLARE

v_contents      text;
r_dataline      record;
v_rows          integer;

BEGIN
   
   PERFORM casesvc.logmessage(p_messagetext := 'GENERATING CASE EVENTS REPORT'
                             ,p_jobid := 0
                             ,p_messagelevel := 'INFO'
                             ,p_functionname := 'casesvc.generate_case_events_report');  
   
      v_rows := 0;
      v_contents    := '';
      v_contents    := 'Sample Unit Ref,Sample Unit Type,Case Ref,Case Created,Action Created,Action Completed,Respondent Account Created,Respondent Enrolled,Access Code Authentication Attempt,Collection Instrument Downloaded,Unsuccessful Response Upload,Successful Response Upload,Offline Response Processed'; -- Set header line    

      FOR r_dataline IN (SELECT
  events.sampleunitref 
, events.sampleunittype
, events.caseref
, events.case_created
, events.action_created
--, events.action_cancellation_created
--, events.action_cancellation_completed
, events.action_completed
--, events.action_updated     
, events.respondent_account_created                                                                                           
, events.respondent_enroled         
, events.access_code_authentication_attempt_ind 
, events.collection_instrument_downloaded_ind 
, events.unsuccessful_response_upload_ind  
, events.successful_response_upload_ind 
, events.offline_response_processed_ind   
  
FROM 
(SELECT 
    cg.sampleunitref
  , c.sampleunittype 
  , c.caseref
  -- response chasing categories
  , MAX(CASE WHEN ce.categoryFK = 'ACCESS_CODE_AUTHENTICATION_ATTEMPT'  THEN 1 ELSE  0 END) access_code_authentication_attempt_ind 	--(B)  -- count distinct event
  , SUM(CASE WHEN ce.categoryFK = 'RESPONDENT_ACCOUNT_CREATED' 		THEN 1 ELSE  0 END) respondent_account_created 			--(B)  -- count all events
  , SUM(CASE WHEN ce.categoryFK = 'RESPONDENT_ENROLED' 			THEN 1 ELSE  0 END) respondent_enroled 				--(B)  -- count all events
  , MAX(CASE WHEN ce.categoryFK = 'COLLECTION_INSTRUMENT_DOWNLOADED'    THEN 1 ELSE  0 END) collection_instrument_downloaded_ind	--(BI) -- count distinct event
  , MAX(CASE WHEN ce.categoryFK = 'SUCCESSFUL_RESPONSE_UPLOAD' 		THEN 1 ELSE  0 END) successful_response_upload_ind		--(BI) -- count distinct event
  -- remaining categories
  , SUM(CASE WHEN ce.categoryFK = 'CASE_CREATED'                        THEN 1 ELSE  0 END) case_created 				--(B,BI) -- count all event
  , SUM(CASE WHEN ce.categoryFK = 'ACTION_CREATED'                      THEN 1 ELSE  0 END) action_created  				--(B,BI) -- count all events
  , SUM(CASE WHEN ce.categoryFK = 'ACTION_CANCELLATION_COMPLETED' 	THEN 1 ELSE  0 END) action_cancellation_completed 		--(B,BI) -- count all events
  , SUM(CASE WHEN ce.categoryFK = 'ACTION_CANCELLATION_CREATED' 	THEN 1 ELSE  0 END) action_cancellation_created 		--(B,BI) -- count all events
  , SUM(CASE WHEN ce.categoryFK = 'ACTION_COMPLETED' 			THEN 1 ELSE  0 END) action_completed 				--(B,BI) -- count all events
  , SUM(CASE WHEN ce.categoryFK = 'ACTION_UPDATED' 			THEN 1 ELSE  0 END) action_updated 				--(B,BI) -- count all events  
  , MAX(CASE WHEN ce.categoryFK = 'OFFLINE_RESPONSE_PROCESSED' 		THEN 1 ELSE  0 END) offline_response_processed_ind		--(BI)	 -- count distinct event
  , MAX(CASE WHEN ce.categoryFK = 'UNSUCCESSFUL_RESPONSE_UPLOAD' 	THEN 1 ELSE  0 END) unsuccessful_response_upload_ind 		--(BI)   -- count distinct event   
FROM   casesvc.caseevent ce
RIGHT OUTER JOIN casesvc.case c  ON c.casePK = ce.caseFK 
INNER JOIN casesvc.casegroup cg  ON c.casegroupFK = cg.casegroupPK
GROUP BY cg.sampleunitref
       , c.sampleunittype
       , c.casePK) events
ORDER BY events.sampleunitref
       , events.sampleunittype
       , events.caseref) LOOP
            v_contents := v_contents || chr(10) || r_dataline.sampleunitref || ',' || r_dataline.sampleunittype || ',' 
            || r_dataline.caseref || ',' 
            || r_dataline.case_created ||',' 
            || r_dataline.action_created ||',' 
            || r_dataline.action_completed ||',' 
            || r_dataline.respondent_account_created ||',' 
            || r_dataline.respondent_enroled ||',' 
            || r_dataline.access_code_authentication_attempt_ind ||',' 
            || r_dataline.collection_instrument_downloaded_ind ||',' 
            || r_dataline.unsuccessful_response_upload_ind ||',' 
            || r_dataline.successful_response_upload_ind ||',' 
            || r_dataline.offline_response_processed_ind ;                                    
            v_rows := v_rows+1;  
      END LOOP;      

      IF v_rows > 0 THEN  
         -- Insert the data into the report table
         INSERT INTO casesvc.report(id, reportPK,reporttypeFK,contents, createddatetime) VALUES(gen_random_uuid(), nextval('casesvc.reportPKseq'), 'CASE_EVENTS', v_contents, CURRENT_TIMESTAMP);
      END IF;

      PERFORM casesvc.logmessage(p_messagetext := 'GENERATING CASE EVENTS REPORT COMPLETED ROWS WRIITEN = ' || v_rows
                                       ,p_jobid := 0
                                       ,p_messagelevel := 'INFO'
                                       ,p_functionname := 'casesvc.generate_case_events_report');
     
   
      PERFORM casesvc.logmessage(p_messagetext := 'CASE EVENTS REPORT GENERATED'
                                       ,p_jobid := 0
                                       ,p_messagelevel := 'INFO'
                                       ,p_functionname := 'casesvc.generate_case_events_report');
 RETURN TRUE;

 EXCEPTION
 WHEN OTHERS THEN  
    PERFORM casesvc.logmessage(p_messagetext := 'GENERATING CASE EVENTS REPORT EXCEPTION TRIGGERED SQLERRM: ' ||

SQLERRM || ' SQLSTATE : ' || SQLSTATE
                              ,p_jobid := 0
                              ,p_messagelevel := 'FATAL'
                              ,p_functionname := 'casesvc.generate_case_events_report');
                             
 RETURN FALSE;
END;
$$;


ALTER FUNCTION casesvc.generate_case_events_report() OWNER TO casesvc;

--
-- Name: generate_response_chasing_report(); Type: FUNCTION; Schema: casesvc; Owner: casesvc
--

CREATE FUNCTION generate_response_chasing_report() RETURNS boolean
    LANGUAGE plpgsql
    AS $$
DECLARE

	v_contents      text;
	r_dataline      record;
	v_rows          integer;

	BEGIN
   
	   PERFORM casesvc.logmessage(p_messagetext := 'GENERATING RESPONSE CHASING REPORT'
	                             ,p_jobid := 0
	                             ,p_messagelevel := 'INFO'
	                             ,p_functionname := 'casesvc.generate_response_chasing_report');  
   
	      v_rows := 0;
	      v_contents    := '';
	      v_contents    := 'Sample Unit Ref,Sample Unit Type,Case Ref,Authentication Attempt No Account Created,Account Created No Enrolment,Collection Instrument Downloaded No Successful Response Upload';   

	      FOR r_dataline IN (SELECT
	  events.sampleunitref
	, events.sampleunittype
	, events.caseref  
	, CASE WHEN events.access_code_authentication_attempt_ind = 1  AND events.respondent_account_created 	 = 0 THEN 1 ELSE 0 END  authentication_attempt_no_account_created  --(B) 
	, (events.respondent_account_created - events.respondent_enroled) account_created_no_enrolment  --(B)  
	, CASE WHEN events.collection_instrument_downloaded_ind   = 1  AND events.successful_response_upload_ind = 0 THEN 1 ELSE 0 END  collection_instrument_downloaded_no_successful_upload --(BI)
	FROM 
	(SELECT 
	    cg.sampleunitref
	  , c.sampleunittype 
	  , c.caseref
	  , MAX(CASE WHEN ce.categoryFK = 'ACCESS_CODE_AUTHENTICATION_ATTEMPT'  THEN 1 ELSE  0 END) access_code_authentication_attempt_ind --(B)  -- count distinct event
	  , SUM(CASE WHEN ce.categoryFK = 'RESPONDENT_ACCOUNT_CREATED' 		THEN 1 ELSE  0 END) respondent_account_created 		   --(B)  -- count all events
	  , SUM(CASE WHEN ce.categoryFK = 'RESPONDENT_ENROLED' 			THEN 1 ELSE  0 END) respondent_enroled 			   --(B)  -- count all events
	  , MAX(CASE WHEN ce.categoryFK = 'COLLECTION_INSTRUMENT_DOWNLOADED'    THEN 1 ELSE  0 END) collection_instrument_downloaded_ind   --(BI) -- count distinct event
	  , MAX(CASE WHEN ce.categoryFK = 'SUCCESSFUL_RESPONSE_UPLOAD' 		THEN 1 ELSE  0 END) successful_response_upload_ind	   --(BI) -- count distinct event 
	FROM casesvc.caseevent ce
	RIGHT OUTER JOIN casesvc.case c  ON c.casePK      = ce.caseFK 
	INNER JOIN casesvc.casegroup cg  ON c.casegroupFK = cg.casegroupPK
	WHERE ce.categoryFK = ANY (ARRAY['ACCESS_CODE_AUTHENTICATION_ATTEMPT','RESPONDENT_ACCOUNT_CREATED','RESPONDENT_ENROLED','COLLECTION_INSTRUMENT_DOWNLOADED','SUCCESSFUL_RESPONSE_UPLOAD'])
	GROUP BY cg.sampleunitref
	       , c.sampleunittype
	       , c.casePK) events
	WHERE (events.access_code_authentication_attempt_ind = 1  AND events.respondent_account_created     = 0)
	OR    (events.collection_instrument_downloaded_ind   = 1  AND events.successful_response_upload_ind = 0)
	OR    (events.respondent_account_created > events.respondent_enroled)
	ORDER BY events.sampleunitref
	       , events.sampleunittype
	       , events.caseref) LOOP
	            v_contents := v_contents || chr(10) || r_dataline.sampleunitref || ',' || r_dataline.sampleunittype || ',' 
	            || r_dataline.caseref || ',' 
	            || r_dataline.authentication_attempt_no_account_created ||',' 
	            || r_dataline.account_created_no_enrolment ||',' 
	            || r_dataline.collection_instrument_downloaded_no_successful_upload ;                                    
	            v_rows := v_rows+1;  
	      END LOOP;      

	      IF v_rows > 0 THEN  
	         -- Insert the data into the report table
	         INSERT INTO casesvc.report(id, reportPK,reporttypeFK,contents, createddatetime) VALUES(gen_random_uuid(), nextval('casesvc.reportPKseq'), 'RESPONSE_CHASING', v_contents, CURRENT_TIMESTAMP);
	      END IF;

	      PERFORM casesvc.logmessage(p_messagetext := 'GENERATING RESPONSE CHASING REPORT COMPLETED ROWS WRIITEN = ' || v_rows
	                                       ,p_jobid := 0
	                                       ,p_messagelevel := 'INFO'
	                                       ,p_functionname := 'casesvc.generate_response_chasing_report');
     
   
	      PERFORM casesvc.logmessage(p_messagetext := 'RESPONSE CHASING REPORT GENERATED'
	                                       ,p_jobid := 0
	                                       ,p_messagelevel := 'INFO'
	                                       ,p_functionname := 'casesvc.generate_response_chasing_report');
	 RETURN TRUE;

	 EXCEPTION
	 WHEN OTHERS THEN  
	    PERFORM casesvc.logmessage(p_messagetext := 'GENERATING RESPONSE CHASING REPORT EXCEPTION TRIGGERED SQLERRM: ' ||

	SQLERRM || ' SQLSTATE : ' || SQLSTATE
	                              ,p_jobid := 0
	                              ,p_messagelevel := 'FATAL'
	                              ,p_functionname := 'casesvc.generate_response_chasing_report');
                             
	 RETURN FALSE;
	END;
	$$;


ALTER FUNCTION casesvc.generate_response_chasing_report() OWNER TO casesvc;

--
-- Name: logmessage(text, numeric, text, text); Type: FUNCTION; Schema: casesvc; Owner: casesvc
--

CREATE FUNCTION logmessage(p_messagetext text DEFAULT NULL::text, p_jobid numeric DEFAULT NULL::numeric, p_messagelevel text DEFAULT NULL::text, p_functionname text DEFAULT NULL::text) RETURNS boolean
    LANGUAGE plpgsql
    AS $$
DECLARE
v_text TEXT ;
v_function TEXT;
BEGIN

INSERT INTO casesvc.messagelog (messagetext, jobid, messagelevel, functionname, createddatetime )
VALUES (p_messagetext, p_jobid, p_messagelevel, p_functionname, current_timestamp);

  RETURN TRUE;
EXCEPTION
WHEN OTHERS THEN
RETURN FALSE;
END;
$$;


ALTER FUNCTION casesvc.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text) OWNER TO casesvc;

SET search_path = collectionexercise, pg_catalog;

--
-- Name: generate_collectionexercise_mi(); Type: FUNCTION; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE FUNCTION generate_collectionexercise_mi() RETURNS boolean
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
DECLARE

v_contents      text;
r_dataline      record;
v_rows          integer;

BEGIN
    
    PERFORM collectionexercise.logmessage(p_messagetext := 'GENERATING COLLECTION EXERCISE MI REPORT'
                              ,p_jobid := 0
                              ,p_messagelevel := 'INFO'
                              ,p_functionname := 'collectionexercise.generate_collectionexercise_mi');  
    
       v_rows     := 0;
       v_contents := '';
       v_contents := 'CE Name,Scheduled Start DateTime,Scheduled Execution DateTime,Scheduled Return DateTime,Scheduled End DateTime,Period Start DateTime,Period End DateTime,Actual Execution DateTime,Actual Publish DateTime,Executed By,State,Sample Size';

-- collectionexercise Report

       FOR r_dataline IN (SELECT  c.name
                                , c.scheduledstartdatetime
                                , c.scheduledexecutiondatetime
                                , c.scheduledreturndatetime
                                , c.scheduledenddatetime
                                , c.periodstartdatetime
                                , c.periodenddatetime
                                , c.actualexecutiondatetime
                                , c.actualpublishdatetime
                                , c.executedby
                                , c.stateFK
                                , c.samplesize 
                          FROM collectionexercise.collectionexercise c) LOOP

                                v_contents := v_contents                                    || chr(10) 
                                || r_dataline.name                                          || ','
                                || COALESCE(r_dataline.scheduledstartdatetime::text,'')     || ','
                                || COALESCE(r_dataline.scheduledexecutiondatetime::text,'') || ','
                                || COALESCE(r_dataline.scheduledreturndatetime::text,'')    || ','
                                || COALESCE(r_dataline.scheduledenddatetime::text,'')       || ','
                                || COALESCE(r_dataline.periodstartdatetime::text,'')        || ','
                                || COALESCE(r_dataline.periodenddatetime::text,'')          || ','
                                || COALESCE(r_dataline.actualexecutiondatetime::text,'')    || ','
                                || COALESCE(r_dataline.actualpublishdatetime ::text,'')     || ','
                                || COALESCE(r_dataline.executedby::text,'')                 || ','
                                || COALESCE(r_dataline.stateFK::text,'')                    || ','
                                || COALESCE(r_dataline.samplesize::text,'');
                              
             v_rows := v_rows+1;  
       END LOOP;       

       -- Insert the data into the report table
       INSERT INTO collectionexercise.report (id, reportPK,reporttypeFK,contents, createddatetime) VALUES(gen_random_uuid(), nextval('collectionexercise.reportPKseq'), 'COLLECTIONEXERCISE', v_contents, CURRENT_TIMESTAMP); 

 
       PERFORM collectionexercise.logmessage(p_messagetext := 'GENERATING COLLECTION EXERCISE MI REPORT COMPLETED ROWS WRIITEN = ' || v_rows
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'collectionexercise.generate_collectionexercise_mi'); 
      
    
       PERFORM collectionexercise.logmessage(p_messagetext := 'COLLECTION EXERCISE MI REPORT GENERATED'
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'collectionexercise.generate_collectionexercise_mi');
  
  RETURN TRUE;

  EXCEPTION
  WHEN OTHERS THEN   
     PERFORM collectionexercise.logmessage(p_messagetext := 'GENERATE REPORTS EXCEPTION TRIGGERED SQLERRM: ' || SQLERRM || ' SQLSTATE : ' || SQLSTATE
                               ,p_jobid := 0
                               ,p_messagelevel := 'FATAL'
                               ,p_functionname := 'collectionexercise.generate_collectionexercise_mi');
                               
  RETURN FALSE;
END;
$$;


ALTER FUNCTION collectionexercise.generate_collectionexercise_mi() OWNER TO collectionexercisesvc;

--
-- Name: logmessage(text, numeric, text, text); Type: FUNCTION; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE FUNCTION logmessage(p_messagetext text DEFAULT NULL::text, p_jobid numeric DEFAULT NULL::numeric, p_messagelevel text DEFAULT NULL::text, p_functionname text DEFAULT NULL::text) RETURNS boolean
    LANGUAGE plpgsql
    AS $$
DECLARE
v_text TEXT ;
v_function TEXT;
BEGIN
INSERT INTO collectionexercise.messagelog
(messagetext, jobid, messagelevel, functionname, createddatetime )
values (p_messagetext, p_jobid, p_messagelevel, p_functionname, current_timestamp);
  RETURN TRUE;
EXCEPTION
WHEN OTHERS THEN
RETURN FALSE;
END;
$$;


ALTER FUNCTION collectionexercise.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text) OWNER TO collectionexercisesvc;

SET search_path = sample, pg_catalog;

--
-- Name: generate_sample_mi(); Type: FUNCTION; Schema: sample; Owner: samplesvc
--

CREATE FUNCTION generate_sample_mi() RETURNS boolean
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
DECLARE

v_contents      text;
r_dataline      record;
v_rows          integer;

BEGIN
    
    PERFORM sample.logmessage(p_messagetext := 'GENERATING SAMPLE MI REPORTS'
                              ,p_jobid := 0
                              ,p_messagelevel := 'INFO'
                              ,p_functionname := 'sample.generate_sample_mi');  
    
       v_rows     := 0;
       v_contents := '';
       v_contents := 'Sample Unit Ref,Form Type';

-- sample Report

       FOR r_dataline IN (SELECT  s.sampleunitref, s.formtype FROM sample.sampleunit s ORDER BY s.sampleunitref) LOOP

                           v_contents := v_contents     || chr(10) 
                           || r_dataline.sampleunitref  || ','
                           || r_dataline.formtype  ;   
             v_rows := v_rows+1;  
       END LOOP;       

       -- Insert the data into the report table
       INSERT INTO sample.report (id, reportPK,reporttypeFK,contents, createddatetime) VALUES(gen_random_uuid(), nextval('sample.reportPKseq'), 'SAMPLE', v_contents, CURRENT_TIMESTAMP); 

               
       PERFORM sample.logmessage(p_messagetext := 'GENERATING SAMPLE MI REPORT COMPLETED ROWS WRIITEN = ' || v_rows
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'sample.generate_sample_mi'); 
      
    
       PERFORM sample.logmessage(p_messagetext := 'SAMPLE MI REPORT GENERATED'
                                        ,p_jobid := 0
                                        ,p_messagelevel := 'INFO'
                                        ,p_functionname := 'sample.generate_sample_mi');
  
  RETURN TRUE;

  EXCEPTION
  WHEN OTHERS THEN   
     PERFORM sample.logmessage(p_messagetext := 'GENERATE REPORTS EXCEPTION TRIGGERED SQLERRM: ' || SQLERRM || ' SQLSTATE : ' || SQLSTATE
                               ,p_jobid := 0
                               ,p_messagelevel := 'FATAL'
                               ,p_functionname := 'sample.generate_sample_mi');
                               
  RETURN FALSE;
END;
$$;


ALTER FUNCTION sample.generate_sample_mi() OWNER TO samplesvc;

--
-- Name: logmessage(text, numeric, text, text); Type: FUNCTION; Schema: sample; Owner: samplesvc
--

CREATE FUNCTION logmessage(p_messagetext text DEFAULT NULL::text, p_jobid numeric DEFAULT NULL::numeric, p_messagelevel text DEFAULT NULL::text, p_functionname text DEFAULT NULL::text) RETURNS boolean
    LANGUAGE plpgsql
    AS $$
DECLARE
v_text TEXT ;
v_function TEXT;
BEGIN
INSERT INTO sample.messagelog
(messagetext, jobid, messagelevel, functionname, createddatetime )
values (p_messagetext, p_jobid, p_messagelevel, p_functionname, current_timestamp);
  RETURN TRUE;
EXCEPTION
WHEN OTHERS THEN
RETURN FALSE;
END;
$$;


ALTER FUNCTION sample.logmessage(p_messagetext text, p_jobid numeric, p_messagelevel text, p_functionname text) OWNER TO samplesvc;

SET search_path = action, pg_catalog;

--
-- Name: actionpkseq; Type: SEQUENCE; Schema: action; Owner: actionsvc
--

CREATE SEQUENCE actionpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE actionpkseq OWNER TO actionsvc;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: action; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE action (
    id uuid NOT NULL,
    actionpk bigint DEFAULT nextval('actionpkseq'::regclass) NOT NULL,
    caseid uuid NOT NULL,
    casefk bigint NOT NULL,
    actionplanfk integer,
    actionrulefk integer,
    actiontypefk integer NOT NULL,
    createdby character varying(50) NOT NULL,
    manuallycreated boolean NOT NULL,
    priority integer DEFAULT 3,
    situation character varying(100),
    statefk character varying(20) NOT NULL,
    createddatetime timestamp with time zone NOT NULL,
    updateddatetime timestamp with time zone,
    optlockversion integer DEFAULT 0
);


ALTER TABLE action OWNER TO actionsvc;

--
-- Name: COLUMN action.priority; Type: COMMENT; Schema: action; Owner: actionsvc
--

COMMENT ON COLUMN action.priority IS '1 = highest, 5 = lowest';


--
-- Name: actionplan; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE actionplan (
    id uuid NOT NULL,
    actionplanpk integer NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(250) NOT NULL,
    createdby character varying(20) NOT NULL,
    lastrundatetime timestamp with time zone
);


ALTER TABLE actionplan OWNER TO actionsvc;

--
-- Name: actionplanjobseq; Type: SEQUENCE; Schema: action; Owner: actionsvc
--

CREATE SEQUENCE actionplanjobseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE actionplanjobseq OWNER TO actionsvc;

--
-- Name: actionplanjob; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE actionplanjob (
    id uuid NOT NULL,
    actionplanjobpk integer DEFAULT nextval('actionplanjobseq'::regclass) NOT NULL,
    actionplanfk integer NOT NULL,
    createdby character varying(20) NOT NULL,
    statefk character varying(20) NOT NULL,
    createddatetime timestamp with time zone NOT NULL,
    updateddatetime timestamp with time zone
);


ALTER TABLE actionplanjob OWNER TO actionsvc;

--
-- Name: actionplanjobstate; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE actionplanjobstate (
    statepk character varying(20) NOT NULL
);


ALTER TABLE actionplanjobstate OWNER TO actionsvc;

--
-- Name: actionrule; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE actionrule (
    actionrulepk integer NOT NULL,
    actionplanfk integer NOT NULL,
    actiontypefk integer NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(250) NOT NULL,
    daysoffset integer NOT NULL,
    priority integer DEFAULT 3
);


ALTER TABLE actionrule OWNER TO actionsvc;

--
-- Name: COLUMN actionrule.priority; Type: COMMENT; Schema: action; Owner: actionsvc
--

COMMENT ON COLUMN actionrule.priority IS '1 = highest, 5 = lowest';


--
-- Name: actionstate; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE actionstate (
    statepk character varying(100) NOT NULL
);


ALTER TABLE actionstate OWNER TO actionsvc;

--
-- Name: actiontype; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE actiontype (
    actiontypepk integer NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(250) NOT NULL,
    handler character varying(100),
    cancancel boolean NOT NULL,
    responserequired boolean
);


ALTER TABLE actiontype OWNER TO actionsvc;

--
-- Name: case; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE "case" (
    actionplanid uuid NOT NULL,
    id uuid NOT NULL,
    casepk bigint NOT NULL,
    actionplanfk integer NOT NULL,
    actionplanstartdate timestamp with time zone NOT NULL,
    actionplanenddate timestamp with time zone NOT NULL
);


ALTER TABLE "case" OWNER TO actionsvc;

--
-- Name: casepkseq; Type: SEQUENCE; Schema: action; Owner: actionsvc
--

CREATE SEQUENCE casepkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE casepkseq OWNER TO actionsvc;

--
-- Name: databasechangelog; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE databasechangelog OWNER TO actionsvc;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE databasechangeloglock OWNER TO actionsvc;

--
-- Name: messageseq; Type: SEQUENCE; Schema: action; Owner: actionsvc
--

CREATE SEQUENCE messageseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE messageseq OWNER TO actionsvc;

--
-- Name: messagelog; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE messagelog (
    messagepk bigint DEFAULT nextval('messageseq'::regclass) NOT NULL,
    messagetext character varying,
    jobid numeric,
    messagelevel character varying,
    functionname character varying,
    createddatetime timestamp with time zone
);


ALTER TABLE messagelog OWNER TO actionsvc;

--
-- Name: outcomecategory; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE outcomecategory (
    handlerpk character varying(100) NOT NULL,
    actionoutcomepk character varying(40) NOT NULL,
    eventcategory character varying(40)
);


ALTER TABLE outcomecategory OWNER TO actionsvc;

--
-- Name: report; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE report (
    id uuid NOT NULL,
    reportpk bigint NOT NULL,
    reporttypefk character varying(20),
    contents text,
    createddatetime timestamp with time zone
);


ALTER TABLE report OWNER TO actionsvc;

--
-- Name: reportpkseq; Type: SEQUENCE; Schema: action; Owner: actionsvc
--

CREATE SEQUENCE reportpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE reportpkseq OWNER TO actionsvc;

--
-- Name: reporttype; Type: TABLE; Schema: action; Owner: actionsvc
--

CREATE TABLE reporttype (
    reporttypepk character varying(20) NOT NULL,
    displayorder integer,
    displayname character varying(40)
);


ALTER TABLE reporttype OWNER TO actionsvc;

SET search_path = actionexporter, pg_catalog;

--
-- Name: actionrequest; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE actionrequest (
    actionrequestpk bigint NOT NULL,
    actionid uuid NOT NULL,
    responserequired boolean DEFAULT false,
    actionplanname character varying(100),
    actiontypename character varying(100) NOT NULL,
    questionset character varying(10),
    contactfk bigint,
    sampleunitreffk character varying(20) NOT NULL,
    caseid uuid NOT NULL,
    priority character varying(10),
    caseref character varying(16),
    iac character varying(24) NOT NULL,
    datestored timestamp with time zone,
    datesent timestamp with time zone,
    exerciseref character varying(20) NOT NULL,
    legalbasis character varying(50),
    region character varying(50),
    respondentstatus character varying(50),
    enrolmentstatus character varying(50),
    casegroupstatus character varying(50),
    surveyref character varying(50)
);


ALTER TABLE actionrequest OWNER TO actionexportersvc;

--
-- Name: actionrequestpkseq; Type: SEQUENCE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE SEQUENCE actionrequestpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE actionrequestpkseq OWNER TO actionexportersvc;

--
-- Name: address; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE address (
    sampleunitrefpk character varying(20) NOT NULL,
    addresstype character varying(6),
    estabtype character varying(6),
    category character varying(20),
    organisation_name character varying(60),
    address_line1 character varying(60),
    address_line2 character varying(60),
    locality character varying(35),
    town_name character varying(30),
    postcode character varying(8),
    lad character varying(9),
    latitude double precision,
    longitude double precision
);


ALTER TABLE address OWNER TO actionexportersvc;

--
-- Name: contactpkseq; Type: SEQUENCE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE SEQUENCE contactpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE contactpkseq OWNER TO actionexportersvc;

--
-- Name: contact; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE contact (
    contactpk integer DEFAULT nextval('contactpkseq'::regclass) NOT NULL,
    forename character varying(35),
    surname character varying(35),
    phonenumber character varying(20),
    emailaddress character varying(50),
    title character varying(20)
);


ALTER TABLE contact OWNER TO actionexportersvc;

--
-- Name: databasechangelog; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE databasechangelog OWNER TO actionexportersvc;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE databasechangeloglock OWNER TO actionexportersvc;

--
-- Name: filerowcount; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE filerowcount (
    filename character varying(100) NOT NULL,
    rowcount integer NOT NULL,
    datesent timestamp with time zone NOT NULL,
    reported boolean NOT NULL,
    sendresult boolean NOT NULL
);


ALTER TABLE filerowcount OWNER TO actionexportersvc;

--
-- Name: messageseq; Type: SEQUENCE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE SEQUENCE messageseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE messageseq OWNER TO actionexportersvc;

--
-- Name: messagelog; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE messagelog (
    messagepk bigint DEFAULT nextval('messageseq'::regclass) NOT NULL,
    messagetext character varying,
    jobid numeric,
    messagelevel character varying,
    functionname character varying,
    createddatetime timestamp with time zone
);


ALTER TABLE messagelog OWNER TO actionexportersvc;

--
-- Name: report; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE report (
    id uuid NOT NULL,
    reportpk bigint NOT NULL,
    reporttypefk character varying(20),
    contents text,
    createddatetime timestamp with time zone
);


ALTER TABLE report OWNER TO actionexportersvc;

--
-- Name: reportpkseq; Type: SEQUENCE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE SEQUENCE reportpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE reportpkseq OWNER TO actionexportersvc;

--
-- Name: reporttype; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE reporttype (
    reporttypepk character varying(20) NOT NULL,
    displayorder integer,
    displayname character varying(40)
);


ALTER TABLE reporttype OWNER TO actionexportersvc;

--
-- Name: template; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE template (
    templatenamepk character varying(100) NOT NULL,
    content text NOT NULL,
    datemodified timestamp with time zone
);


ALTER TABLE template OWNER TO actionexportersvc;

--
-- Name: templatemapping; Type: TABLE; Schema: actionexporter; Owner: actionexportersvc
--

CREATE TABLE templatemapping (
    actiontypenamepk character varying(100) NOT NULL,
    templatenamefk character varying(100) NOT NULL,
    filenameprefix character varying(100) NOT NULL,
    datemodified timestamp with time zone
);


ALTER TABLE templatemapping OWNER TO actionexportersvc;

SET search_path = casesvc, pg_catalog;

--
-- Name: caserefseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE caserefseq
    START WITH 1000000000000001
    INCREMENT BY 1
    MINVALUE 1000000000000001
    MAXVALUE 9999999999999999
    CACHE 1;


ALTER TABLE caserefseq OWNER TO casesvc;

--
-- Name: case; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE "case" (
    casepk bigint NOT NULL,
    id uuid NOT NULL,
    caseref character varying(16) DEFAULT nextval('caserefseq'::regclass),
    casegroupfk bigint NOT NULL,
    casegroupid uuid NOT NULL,
    partyid uuid,
    sampleunittype character varying(2),
    collectioninstrumentid uuid,
    statefk character varying(20),
    actionplanid uuid,
    createddatetime timestamp with time zone,
    createdby character varying(50),
    iac character varying(20),
    sourcecase bigint,
    optlockversion integer DEFAULT 0
);


ALTER TABLE "case" OWNER TO casesvc;

--
-- Name: caseevent; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE caseevent (
    caseeventpk bigint NOT NULL,
    casefk bigint NOT NULL,
    description character varying(350),
    createdby character varying(50),
    createddatetime timestamp with time zone,
    categoryfk character varying(40),
    subcategory character varying(100)
);


ALTER TABLE caseevent OWNER TO casesvc;

--
-- Name: caseeventseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE caseeventseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE caseeventseq OWNER TO casesvc;

--
-- Name: casegroup; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE casegroup (
    casegrouppk bigint NOT NULL,
    id uuid NOT NULL,
    partyid uuid,
    collectionexerciseid uuid,
    sampleunitref character varying(20),
    sampleunittype character varying(2),
    status character varying(20) NOT NULL
);


ALTER TABLE casegroup OWNER TO casesvc;

--
-- Name: casegroupseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE casegroupseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE casegroupseq OWNER TO casesvc;

--
-- Name: casegroupstatusaudit; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE casegroupstatusaudit (
    casegroupstatusauditpk bigint NOT NULL,
    casegroupfk bigint NOT NULL,
    partyid uuid,
    status character varying(20),
    createddatetime timestamp with time zone
);


ALTER TABLE casegroupstatusaudit OWNER TO casesvc;

--
-- Name: casegroupstatusauditseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE casegroupstatusauditseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE casegroupstatusauditseq OWNER TO casesvc;

--
-- Name: caseseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE caseseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE caseseq OWNER TO casesvc;

--
-- Name: casestate; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE casestate (
    statepk character varying(20) NOT NULL
);


ALTER TABLE casestate OWNER TO casesvc;

--
-- Name: category; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE category (
    categorypk character varying(40) NOT NULL,
    shortdescription character varying(50),
    longdescription character varying(50),
    eventtype character varying(20),
    role character varying(100),
    generatedactiontype character varying(100),
    "group" character varying(20),
    oldcasesampleunittypes character varying(10) NOT NULL,
    newcasesampleunittype character varying(10),
    recalccollectioninstrument boolean
);


ALTER TABLE category OWNER TO casesvc;

--
-- Name: databasechangelog; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE databasechangelog OWNER TO casesvc;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE databasechangeloglock OWNER TO casesvc;

--
-- Name: messagelogseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE messagelogseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE messagelogseq OWNER TO casesvc;

--
-- Name: messagelog; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE messagelog (
    messagelogpk bigint DEFAULT nextval('messagelogseq'::regclass) NOT NULL,
    messagetext character varying,
    jobid numeric,
    messagelevel character varying,
    functionname character varying,
    createddatetime timestamp with time zone
);


ALTER TABLE messagelog OWNER TO casesvc;

--
-- Name: report; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE report (
    id uuid NOT NULL,
    reportpk bigint NOT NULL,
    reporttypefk character varying(20),
    contents text,
    createddatetime timestamp with time zone
);


ALTER TABLE report OWNER TO casesvc;

--
-- Name: reportpkseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE reportpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE reportpkseq OWNER TO casesvc;

--
-- Name: reporttype; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE reporttype (
    reporttypepk character varying(20) NOT NULL,
    displayorder integer,
    displayname character varying(40)
);


ALTER TABLE reporttype OWNER TO casesvc;

--
-- Name: response; Type: TABLE; Schema: casesvc; Owner: casesvc
--

CREATE TABLE response (
    responsepk bigint NOT NULL,
    casefk bigint NOT NULL,
    inboundchannel character varying(10),
    responsedatetime timestamp with time zone
);


ALTER TABLE response OWNER TO casesvc;

--
-- Name: responseseq; Type: SEQUENCE; Schema: casesvc; Owner: casesvc
--

CREATE SEQUENCE responseseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE responseseq OWNER TO casesvc;

SET search_path = collectionexercise, pg_catalog;

--
-- Name: casetypedefault; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE casetypedefault (
    casetypedefaultpk integer NOT NULL,
    sampleunittypefk character varying(2) NOT NULL,
    actionplanid uuid,
    survey_uuid uuid
);


ALTER TABLE casetypedefault OWNER TO collectionexercisesvc;

--
-- Name: casetypeoverride; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE casetypeoverride (
    casetypeoverridepk integer NOT NULL,
    exercisefk bigint NOT NULL,
    sampleunittypefk character varying(2) NOT NULL,
    actionplanid uuid
);


ALTER TABLE casetypeoverride OWNER TO collectionexercisesvc;

--
-- Name: exercisepkseq; Type: SEQUENCE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE SEQUENCE exercisepkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE exercisepkseq OWNER TO collectionexercisesvc;

--
-- Name: collectionexercise; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE collectionexercise (
    id uuid NOT NULL,
    exercisepk bigint DEFAULT nextval('exercisepkseq'::regclass) NOT NULL,
    name character varying(20),
    scheduledstartdatetime timestamp with time zone,
    scheduledexecutiondatetime timestamp with time zone,
    scheduledreturndatetime timestamp with time zone,
    scheduledenddatetime timestamp with time zone,
    periodstartdatetime timestamp with time zone,
    periodenddatetime timestamp with time zone,
    actualexecutiondatetime timestamp with time zone,
    actualpublishdatetime timestamp with time zone,
    executedby character varying(50),
    statefk character varying(20) NOT NULL,
    samplesize integer,
    exerciseref character varying(20) NOT NULL,
    user_description character varying(50),
    created timestamp without time zone,
    updated timestamp without time zone,
    deleted boolean DEFAULT false,
    survey_uuid uuid
);


ALTER TABLE collectionexercise OWNER TO collectionexercisesvc;

--
-- Name: collectionexercisestate; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE collectionexercisestate (
    statepk character varying(20) NOT NULL
);


ALTER TABLE collectionexercisestate OWNER TO collectionexercisesvc;

--
-- Name: databasechangelog; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE databasechangelog OWNER TO collectionexercisesvc;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE databasechangeloglock OWNER TO collectionexercisesvc;

--
-- Name: event; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE event (
    id uuid,
    eventpk bigint NOT NULL,
    collexfk bigint NOT NULL,
    tag character varying(20),
    "timestamp" timestamp without time zone,
    created timestamp without time zone,
    updated timestamp without time zone,
    deleted boolean,
    message_sent timestamp without time zone
);


ALTER TABLE event OWNER TO collectionexercisesvc;

--
-- Name: eventpkseq; Type: SEQUENCE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE SEQUENCE eventpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE eventpkseq OWNER TO collectionexercisesvc;

--
-- Name: messagelogseq; Type: SEQUENCE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE SEQUENCE messagelogseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE messagelogseq OWNER TO collectionexercisesvc;

--
-- Name: messagelog; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE messagelog (
    messagelogpk bigint DEFAULT nextval('messagelogseq'::regclass) NOT NULL,
    messagetext character varying,
    jobid numeric,
    messagelevel character varying,
    functionname character varying,
    createddatetime timestamp with time zone
);


ALTER TABLE messagelog OWNER TO collectionexercisesvc;

--
-- Name: report; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE report (
    id uuid NOT NULL,
    reportpk bigint NOT NULL,
    reporttypefk character varying(20),
    contents text,
    createddatetime timestamp with time zone
);


ALTER TABLE report OWNER TO collectionexercisesvc;

--
-- Name: reportpkseq; Type: SEQUENCE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE SEQUENCE reportpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE reportpkseq OWNER TO collectionexercisesvc;

--
-- Name: reporttype; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE reporttype (
    reporttypepk character varying(20) NOT NULL,
    displayorder integer,
    displayname character varying(40)
);


ALTER TABLE reporttype OWNER TO collectionexercisesvc;

--
-- Name: samplelink; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE samplelink (
    collectionexerciseid uuid,
    samplesummaryid uuid,
    samplelinkpk bigint NOT NULL
);


ALTER TABLE samplelink OWNER TO collectionexercisesvc;

--
-- Name: samplelinkpkseq; Type: SEQUENCE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE SEQUENCE samplelinkpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE samplelinkpkseq OWNER TO collectionexercisesvc;

--
-- Name: sampleunitpkseq; Type: SEQUENCE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE SEQUENCE sampleunitpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE sampleunitpkseq OWNER TO collectionexercisesvc;

--
-- Name: sampleunit; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE sampleunit (
    sampleunitpk bigint DEFAULT nextval('sampleunitpkseq'::regclass) NOT NULL,
    sampleunitgroupfk bigint NOT NULL,
    collectioninstrumentid uuid,
    partyid uuid,
    sampleunitref character varying(20) NOT NULL,
    sampleunittypefk character varying(2) NOT NULL
);


ALTER TABLE sampleunit OWNER TO collectionexercisesvc;

--
-- Name: sampleunitgrouppkseq; Type: SEQUENCE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE SEQUENCE sampleunitgrouppkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE sampleunitgrouppkseq OWNER TO collectionexercisesvc;

--
-- Name: sampleunitgroup; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE sampleunitgroup (
    sampleunitgrouppk bigint DEFAULT nextval('sampleunitgrouppkseq'::regclass) NOT NULL,
    exercisefk bigint NOT NULL,
    formtype character varying(10) NOT NULL,
    statefk character varying(20) NOT NULL,
    createddatetime timestamp with time zone,
    modifieddatetime timestamp with time zone
);


ALTER TABLE sampleunitgroup OWNER TO collectionexercisesvc;

--
-- Name: sampleunitgroupstate; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE sampleunitgroupstate (
    statepk character varying(20) NOT NULL
);


ALTER TABLE sampleunitgroupstate OWNER TO collectionexercisesvc;

--
-- Name: sampleunittype; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE sampleunittype (
    sampleunittypepk character varying(2) NOT NULL
);


ALTER TABLE sampleunittype OWNER TO collectionexercisesvc;

--
-- Name: survey; Type: TABLE; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE TABLE survey (
    id uuid NOT NULL,
    surveypk integer NOT NULL,
    surveyref character varying(100) NOT NULL
);


ALTER TABLE survey OWNER TO collectionexercisesvc;

SET search_path = iac, pg_catalog;

--
-- Name: databasechangelog; Type: TABLE; Schema: iac; Owner: postgres
--

CREATE TABLE databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE databasechangelog OWNER TO postgres;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: iac; Owner: postgres
--

CREATE TABLE databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE databasechangeloglock OWNER TO postgres;

--
-- Name: iac; Type: TABLE; Schema: iac; Owner: postgres
--

CREATE TABLE iac (
    code character varying(20) NOT NULL,
    active boolean DEFAULT true NOT NULL,
    createddatetime timestamp with time zone NOT NULL,
    createdby character varying(20) NOT NULL,
    updateddatetime timestamp with time zone,
    updatedby character varying(20),
    lastuseddatetime timestamp with time zone
);


ALTER TABLE iac OWNER TO postgres;

SET search_path = notifygatewaysvc, pg_catalog;

--
-- Name: databasechangelog; Type: TABLE; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

CREATE TABLE databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE databasechangelog OWNER TO notifygatewaysvc;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

CREATE TABLE databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE databasechangeloglock OWNER TO notifygatewaysvc;

--
-- Name: message; Type: TABLE; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

CREATE TABLE message (
    messagepk bigint NOT NULL,
    id uuid NOT NULL,
    notificationid character varying(128),
    optlockversion integer DEFAULT 0
);


ALTER TABLE message OWNER TO notifygatewaysvc;

--
-- Name: messageseq; Type: SEQUENCE; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

CREATE SEQUENCE messageseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE messageseq OWNER TO notifygatewaysvc;

SET search_path = partysvc, pg_catalog;

--
-- Name: alembic_version; Type: TABLE; Schema: partysvc; Owner: postgres
--

CREATE TABLE alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE alembic_version OWNER TO postgres;

--
-- Name: business; Type: TABLE; Schema: partysvc; Owner: postgres
--

CREATE TABLE business (
    party_uuid uuid NOT NULL,
    business_ref text,
    created_on timestamp without time zone
);


ALTER TABLE business OWNER TO postgres;

--
-- Name: business_attributes; Type: TABLE; Schema: partysvc; Owner: postgres
--

CREATE TABLE business_attributes (
    id integer NOT NULL,
    business_id uuid,
    sample_summary_id text,
    collection_exercise text,
    attributes jsonb,
    created_on timestamp without time zone
);


ALTER TABLE business_attributes OWNER TO postgres;

--
-- Name: business_attributes_id_seq; Type: SEQUENCE; Schema: partysvc; Owner: postgres
--

CREATE SEQUENCE business_attributes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE business_attributes_id_seq OWNER TO postgres;

--
-- Name: business_attributes_id_seq; Type: SEQUENCE OWNED BY; Schema: partysvc; Owner: postgres
--

ALTER SEQUENCE business_attributes_id_seq OWNED BY business_attributes.id;


--
-- Name: business_respondent; Type: TABLE; Schema: partysvc; Owner: postgres
--

CREATE TABLE business_respondent (
    business_id uuid NOT NULL,
    respondent_id integer NOT NULL,
    status public.businessrespondentstatus,
    effective_from timestamp without time zone,
    effective_to timestamp without time zone,
    created_on timestamp without time zone
);


ALTER TABLE business_respondent OWNER TO postgres;

--
-- Name: enrolment; Type: TABLE; Schema: partysvc; Owner: postgres
--

CREATE TABLE enrolment (
    business_id uuid NOT NULL,
    respondent_id integer NOT NULL,
    survey_id text NOT NULL,
    survey_name text,
    status public.enrolmentstatus,
    created_on timestamp without time zone
);


ALTER TABLE enrolment OWNER TO postgres;

--
-- Name: pending_enrolment; Type: TABLE; Schema: partysvc; Owner: postgres
--

CREATE TABLE pending_enrolment (
    id integer NOT NULL,
    case_id uuid,
    respondent_id integer,
    business_id uuid,
    survey_id uuid,
    created_on timestamp without time zone
);


ALTER TABLE pending_enrolment OWNER TO postgres;

--
-- Name: pending_enrolment_id_seq; Type: SEQUENCE; Schema: partysvc; Owner: postgres
--

CREATE SEQUENCE pending_enrolment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE pending_enrolment_id_seq OWNER TO postgres;

--
-- Name: pending_enrolment_id_seq; Type: SEQUENCE OWNED BY; Schema: partysvc; Owner: postgres
--

ALTER SEQUENCE pending_enrolment_id_seq OWNED BY pending_enrolment.id;


--
-- Name: respondent; Type: TABLE; Schema: partysvc; Owner: postgres
--

CREATE TABLE respondent (
    id integer NOT NULL,
    party_uuid uuid,
    status public.respondentstatus,
    email_address text,
    first_name text,
    last_name text,
    telephone text,
    created_on timestamp without time zone
);


ALTER TABLE respondent OWNER TO postgres;

--
-- Name: respondent_id_seq; Type: SEQUENCE; Schema: partysvc; Owner: postgres
--

CREATE SEQUENCE respondent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE respondent_id_seq OWNER TO postgres;

--
-- Name: respondent_id_seq; Type: SEQUENCE OWNED BY; Schema: partysvc; Owner: postgres
--

ALTER SEQUENCE respondent_id_seq OWNED BY respondent.id;


SET search_path = public, pg_catalog;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: authz_approvals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE authz_approvals (
    user_id character varying(36) NOT NULL,
    client_id character varying(255) NOT NULL,
    scope character varying(255) NOT NULL,
    expiresat timestamp without time zone DEFAULT now() NOT NULL,
    status character varying(50) DEFAULT 'APPROVED'::character varying NOT NULL,
    lastmodifiedat timestamp without time zone DEFAULT now() NOT NULL,
    identity_zone_id character varying(36)
);


ALTER TABLE authz_approvals OWNER TO postgres;

--
-- Name: credentials_oauthclient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE credentials_oauthclient (
    id integer NOT NULL,
    password character varying(160) NOT NULL,
    client_id character varying(254) NOT NULL,
    redirect_uri character varying(254) NOT NULL
);


ALTER TABLE credentials_oauthclient OWNER TO postgres;

--
-- Name: credentials_oauthclient_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE credentials_oauthclient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE credentials_oauthclient_id_seq OWNER TO postgres;

--
-- Name: credentials_oauthclient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE credentials_oauthclient_id_seq OWNED BY credentials_oauthclient.id;


--
-- Name: credentials_oauthuser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE credentials_oauthuser (
    id integer NOT NULL,
    password character varying(160) NOT NULL,
    email character varying(254) NOT NULL,
    failed_logins integer NOT NULL,
    account_is_locked boolean NOT NULL,
    account_is_verified boolean NOT NULL
);


ALTER TABLE credentials_oauthuser OWNER TO postgres;

--
-- Name: credentials_oauthuser_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE credentials_oauthuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE credentials_oauthuser_id_seq OWNER TO postgres;

--
-- Name: credentials_oauthuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE credentials_oauthuser_id_seq OWNED BY credentials_oauthuser.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO postgres;

--
-- Name: expiring_code_store; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE expiring_code_store (
    code character varying(255) NOT NULL,
    expiresat bigint NOT NULL,
    data text NOT NULL,
    intent text,
    identity_zone_id character varying(36) DEFAULT 'uaa'::character varying NOT NULL
);


ALTER TABLE expiring_code_store OWNER TO postgres;

--
-- Name: external_group_mapping; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE external_group_mapping (
    group_id character varying(36) NOT NULL,
    external_group character varying(255) NOT NULL,
    added timestamp without time zone DEFAULT now() NOT NULL,
    origin character varying(36),
    identity_zone_id character varying(36)
);


ALTER TABLE external_group_mapping OWNER TO postgres;

--
-- Name: group_membership; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE group_membership (
    group_id character varying(36) NOT NULL,
    member_id character varying(36) NOT NULL,
    member_type character varying(8) DEFAULT 'USER'::character varying NOT NULL,
    authorities character varying(255) DEFAULT 'READ'::character varying,
    added timestamp without time zone DEFAULT now() NOT NULL,
    origin character varying(36) DEFAULT 'uaa'::character varying NOT NULL,
    identity_zone_id character varying(36)
);


ALTER TABLE group_membership OWNER TO postgres;

--
-- Name: groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE groups (
    id character varying(36) NOT NULL,
    displayname character varying(255) NOT NULL,
    created timestamp without time zone DEFAULT now() NOT NULL,
    lastmodified timestamp without time zone DEFAULT now() NOT NULL,
    version bigint DEFAULT 0 NOT NULL,
    identity_zone_id character varying(36) DEFAULT 'uaa'::character varying NOT NULL,
    description character varying(255)
);


ALTER TABLE groups OWNER TO postgres;

--
-- Name: identity_provider; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE identity_provider (
    id character varying(36) NOT NULL,
    created timestamp without time zone DEFAULT now(),
    lastmodified timestamp without time zone DEFAULT now(),
    version bigint DEFAULT 0,
    identity_zone_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    origin_key character varying(36) NOT NULL,
    type character varying(255) NOT NULL,
    config text,
    active boolean DEFAULT true NOT NULL
);


ALTER TABLE identity_provider OWNER TO postgres;

--
-- Name: identity_zone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE identity_zone (
    id character varying(36) NOT NULL,
    created timestamp without time zone DEFAULT now(),
    lastmodified timestamp without time zone DEFAULT now(),
    version bigint DEFAULT 0,
    subdomain character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    config text
);


ALTER TABLE identity_zone OWNER TO postgres;

--
-- Name: mfa_providers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE mfa_providers (
    id character varying(36) NOT NULL,
    created timestamp without time zone DEFAULT now() NOT NULL,
    lastmodified timestamp without time zone,
    identity_zone_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    type character varying(255) NOT NULL,
    config text
);


ALTER TABLE mfa_providers OWNER TO postgres;

--
-- Name: oauth_client_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE oauth_client_details (
    client_id character varying(255) NOT NULL,
    resource_ids character varying(1024),
    client_secret character varying(256),
    scope text,
    authorized_grant_types character varying(256),
    web_server_redirect_uri character varying(1024),
    authorities text,
    access_token_validity integer,
    refresh_token_validity integer DEFAULT 0,
    additional_information character varying(4096),
    autoapprove character varying(1024) DEFAULT NULL::character varying,
    identity_zone_id character varying(36) DEFAULT 'uaa'::character varying NOT NULL,
    lastmodified timestamp without time zone DEFAULT now() NOT NULL,
    show_on_home_page boolean DEFAULT true NOT NULL,
    app_launch_url character varying(1024),
    app_icon bytea,
    created_by character(36) DEFAULT NULL::bpchar,
    required_user_groups character varying(1024)
);


ALTER TABLE oauth_client_details OWNER TO postgres;

--
-- Name: oauth_code; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE oauth_code (
    code character varying(256),
    authentication bytea,
    created timestamp without time zone DEFAULT now() NOT NULL,
    expiresat bigint DEFAULT 0 NOT NULL,
    user_id character varying(36),
    client_id character varying(255),
    identity_zone_id character varying(36)
);


ALTER TABLE oauth_code OWNER TO postgres;

--
-- Name: revocable_tokens; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE revocable_tokens (
    token_id character varying(36) NOT NULL,
    client_id character varying(255) NOT NULL,
    user_id character varying(36),
    format character varying(255),
    response_type character varying(25) NOT NULL,
    issued_at bigint NOT NULL,
    expires_at bigint NOT NULL,
    scope text,
    data text NOT NULL,
    identity_zone_id character varying(36) DEFAULT 'uaa'::character varying NOT NULL
);


ALTER TABLE revocable_tokens OWNER TO postgres;

--
-- Name: schema_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE schema_version (
    installed_rank integer NOT NULL,
    version character varying(50),
    description character varying(200) NOT NULL,
    type character varying(20) NOT NULL,
    script character varying(1000) NOT NULL,
    checksum integer,
    installed_by character varying(100) NOT NULL,
    installed_on timestamp without time zone DEFAULT now() NOT NULL,
    execution_time integer NOT NULL,
    success boolean NOT NULL
);


ALTER TABLE schema_version OWNER TO postgres;

--
-- Name: sec_audit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE sec_audit (
    principal_id character varying(255) NOT NULL,
    event_type integer NOT NULL,
    origin character varying(255) NOT NULL,
    event_data character varying(255),
    created timestamp without time zone DEFAULT now(),
    identity_zone_id character varying(36) DEFAULT 'uaa'::character varying
);


ALTER TABLE sec_audit OWNER TO postgres;

--
-- Name: service_provider; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE service_provider (
    id character varying(36) NOT NULL,
    created timestamp without time zone DEFAULT now() NOT NULL,
    lastmodified timestamp without time zone DEFAULT now() NOT NULL,
    version bigint DEFAULT 0,
    identity_zone_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    entity_id character varying(255) NOT NULL,
    config text,
    active boolean DEFAULT true NOT NULL
);


ALTER TABLE service_provider OWNER TO postgres;

--
-- Name: tokens_oauthaccesstoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE tokens_oauthaccesstoken (
    id integer NOT NULL,
    expires_at timestamp with time zone NOT NULL,
    access_token character varying(40) NOT NULL,
    client_id integer NOT NULL,
    refresh_token_id integer,
    user_id integer
);


ALTER TABLE tokens_oauthaccesstoken OWNER TO postgres;

--
-- Name: tokens_oauthaccesstoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tokens_oauthaccesstoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tokens_oauthaccesstoken_id_seq OWNER TO postgres;

--
-- Name: tokens_oauthaccesstoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tokens_oauthaccesstoken_id_seq OWNED BY tokens_oauthaccesstoken.id;


--
-- Name: tokens_oauthaccesstoken_scopes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE tokens_oauthaccesstoken_scopes (
    id integer NOT NULL,
    oauthaccesstoken_id integer NOT NULL,
    oauthscope_id integer NOT NULL
);


ALTER TABLE tokens_oauthaccesstoken_scopes OWNER TO postgres;

--
-- Name: tokens_oauthaccesstoken_scopes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tokens_oauthaccesstoken_scopes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tokens_oauthaccesstoken_scopes_id_seq OWNER TO postgres;

--
-- Name: tokens_oauthaccesstoken_scopes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tokens_oauthaccesstoken_scopes_id_seq OWNED BY tokens_oauthaccesstoken_scopes.id;


--
-- Name: tokens_oauthauthorizationcode; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE tokens_oauthauthorizationcode (
    id integer NOT NULL,
    expires_at timestamp with time zone NOT NULL,
    code character varying(40) NOT NULL,
    redirect_uri character varying(200),
    client_id integer NOT NULL,
    user_id integer
);


ALTER TABLE tokens_oauthauthorizationcode OWNER TO postgres;

--
-- Name: tokens_oauthauthorizationcode_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tokens_oauthauthorizationcode_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tokens_oauthauthorizationcode_id_seq OWNER TO postgres;

--
-- Name: tokens_oauthauthorizationcode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tokens_oauthauthorizationcode_id_seq OWNED BY tokens_oauthauthorizationcode.id;


--
-- Name: tokens_oauthauthorizationcode_scopes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE tokens_oauthauthorizationcode_scopes (
    id integer NOT NULL,
    oauthauthorizationcode_id integer NOT NULL,
    oauthscope_id integer NOT NULL
);


ALTER TABLE tokens_oauthauthorizationcode_scopes OWNER TO postgres;

--
-- Name: tokens_oauthauthorizationcode_scopes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tokens_oauthauthorizationcode_scopes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tokens_oauthauthorizationcode_scopes_id_seq OWNER TO postgres;

--
-- Name: tokens_oauthauthorizationcode_scopes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tokens_oauthauthorizationcode_scopes_id_seq OWNED BY tokens_oauthauthorizationcode_scopes.id;


--
-- Name: tokens_oauthrefreshtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE tokens_oauthrefreshtoken (
    id integer NOT NULL,
    expires_at timestamp with time zone NOT NULL,
    refresh_token character varying(40) NOT NULL
);


ALTER TABLE tokens_oauthrefreshtoken OWNER TO postgres;

--
-- Name: tokens_oauthrefreshtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tokens_oauthrefreshtoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tokens_oauthrefreshtoken_id_seq OWNER TO postgres;

--
-- Name: tokens_oauthrefreshtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tokens_oauthrefreshtoken_id_seq OWNED BY tokens_oauthrefreshtoken.id;


--
-- Name: tokens_oauthscope; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE tokens_oauthscope (
    id integer NOT NULL,
    scope character varying(200) NOT NULL,
    description text NOT NULL,
    is_default boolean NOT NULL
);


ALTER TABLE tokens_oauthscope OWNER TO postgres;

--
-- Name: tokens_oauthscope_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tokens_oauthscope_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tokens_oauthscope_id_seq OWNER TO postgres;

--
-- Name: tokens_oauthscope_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tokens_oauthscope_id_seq OWNED BY tokens_oauthscope.id;


--
-- Name: user_google_mfa_credentials; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE user_google_mfa_credentials (
    user_id character varying(36) NOT NULL,
    secret_key character varying(255) NOT NULL,
    validation_code integer NOT NULL,
    scratch_codes character varying(255) NOT NULL,
    mfa_provider_id character(36) NOT NULL,
    zone_id character(36) NOT NULL
);


ALTER TABLE user_google_mfa_credentials OWNER TO postgres;

--
-- Name: user_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE user_info (
    user_id character varying(36) NOT NULL,
    info text NOT NULL
);


ALTER TABLE user_info OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE users (
    id character(36) NOT NULL,
    created timestamp without time zone DEFAULT now() NOT NULL,
    lastmodified timestamp without time zone DEFAULT now() NOT NULL,
    version bigint DEFAULT 0 NOT NULL,
    username character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    givenname character varying(255),
    familyname character varying(255),
    active boolean DEFAULT true,
    phonenumber character varying(255),
    authorities character varying(1024) DEFAULT 'uaa.user'::character varying,
    verified boolean DEFAULT false NOT NULL,
    origin character varying(36) DEFAULT 'uaa'::character varying NOT NULL,
    external_id character varying(255) DEFAULT NULL::character varying,
    identity_zone_id character varying(36) DEFAULT 'uaa'::character varying NOT NULL,
    salt character varying(36) DEFAULT NULL::character varying,
    passwd_lastmodified timestamp without time zone,
    legacy_verification_behavior boolean DEFAULT false NOT NULL,
    passwd_change_required boolean DEFAULT false NOT NULL,
    last_logon_success_time bigint,
    previous_logon_success_time bigint
);


ALTER TABLE users OWNER TO postgres;

SET search_path = ras_ci, pg_catalog;

--
-- Name: alembic_version; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE alembic_version OWNER TO postgres;

--
-- Name: business; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE business (
    id integer NOT NULL,
    ru_ref character varying(32)
);


ALTER TABLE business OWNER TO postgres;

--
-- Name: business_id_seq; Type: SEQUENCE; Schema: ras_ci; Owner: postgres
--

CREATE SEQUENCE business_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE business_id_seq OWNER TO postgres;

--
-- Name: business_id_seq; Type: SEQUENCE OWNED BY; Schema: ras_ci; Owner: postgres
--

ALTER SEQUENCE business_id_seq OWNED BY business.id;


--
-- Name: exercise; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE exercise (
    id integer NOT NULL,
    exercise_id uuid,
    items integer,
    status public.status
);


ALTER TABLE exercise OWNER TO postgres;

--
-- Name: exercise_id_seq; Type: SEQUENCE; Schema: ras_ci; Owner: postgres
--

CREATE SEQUENCE exercise_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE exercise_id_seq OWNER TO postgres;

--
-- Name: exercise_id_seq; Type: SEQUENCE OWNED BY; Schema: ras_ci; Owner: postgres
--

ALTER SEQUENCE exercise_id_seq OWNED BY exercise.id;


--
-- Name: instrument; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE instrument (
    id integer NOT NULL,
    type character varying(8),
    instrument_id uuid,
    stamp timestamp without time zone,
    survey_id integer,
    classifiers jsonb
);


ALTER TABLE instrument OWNER TO postgres;

--
-- Name: instrument_business; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE instrument_business (
    instrument_id integer,
    business_id integer
);


ALTER TABLE instrument_business OWNER TO postgres;

--
-- Name: instrument_exercise; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE instrument_exercise (
    instrument_id integer,
    exercise_id integer
);


ALTER TABLE instrument_exercise OWNER TO postgres;

--
-- Name: instrument_id_seq; Type: SEQUENCE; Schema: ras_ci; Owner: postgres
--

CREATE SEQUENCE instrument_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE instrument_id_seq OWNER TO postgres;

--
-- Name: instrument_id_seq; Type: SEQUENCE OWNED BY; Schema: ras_ci; Owner: postgres
--

ALTER SEQUENCE instrument_id_seq OWNED BY instrument.id;


--
-- Name: seft_instrument; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE seft_instrument (
    id integer NOT NULL,
    file_name character varying(32),
    data bytea,
    len integer,
    instrument_id uuid
);


ALTER TABLE seft_instrument OWNER TO postgres;

--
-- Name: seft_instrument_id_seq; Type: SEQUENCE; Schema: ras_ci; Owner: postgres
--

CREATE SEQUENCE seft_instrument_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE seft_instrument_id_seq OWNER TO postgres;

--
-- Name: seft_instrument_id_seq; Type: SEQUENCE OWNED BY; Schema: ras_ci; Owner: postgres
--

ALTER SEQUENCE seft_instrument_id_seq OWNED BY seft_instrument.id;


--
-- Name: survey; Type: TABLE; Schema: ras_ci; Owner: postgres
--

CREATE TABLE survey (
    id integer NOT NULL,
    survey_id uuid
);


ALTER TABLE survey OWNER TO postgres;

--
-- Name: survey_id_seq; Type: SEQUENCE; Schema: ras_ci; Owner: postgres
--

CREATE SEQUENCE survey_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE survey_id_seq OWNER TO postgres;

--
-- Name: survey_id_seq; Type: SEQUENCE OWNED BY; Schema: ras_ci; Owner: postgres
--

ALTER SEQUENCE survey_id_seq OWNED BY survey.id;


SET search_path = sample, pg_catalog;

--
-- Name: collectionexercisejob; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE collectionexercisejob (
    collectionexercisejobpk bigint NOT NULL,
    collectionexerciseid uuid,
    surveyref character varying(100),
    exercisedatetime timestamp with time zone,
    createddatetime timestamp with time zone,
    samplesummaryid uuid
);


ALTER TABLE collectionexercisejob OWNER TO samplesvc;

--
-- Name: collectionexercisejobseq; Type: SEQUENCE; Schema: sample; Owner: samplesvc
--

CREATE SEQUENCE collectionexercisejobseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE collectionexercisejobseq OWNER TO samplesvc;

--
-- Name: databasechangelog; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE databasechangelog OWNER TO samplesvc;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE databasechangeloglock OWNER TO samplesvc;

--
-- Name: messagelogseq; Type: SEQUENCE; Schema: sample; Owner: samplesvc
--

CREATE SEQUENCE messagelogseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE messagelogseq OWNER TO samplesvc;

--
-- Name: messagelog; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE messagelog (
    messagelogpk bigint DEFAULT nextval('messagelogseq'::regclass) NOT NULL,
    messagetext character varying,
    jobid numeric,
    messagelevel character varying,
    functionname character varying,
    createddatetime timestamp with time zone
);


ALTER TABLE messagelog OWNER TO samplesvc;

--
-- Name: report; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE report (
    id uuid NOT NULL,
    reportpk bigint NOT NULL,
    reporttypefk character varying(20),
    contents text,
    createddatetime timestamp with time zone
);


ALTER TABLE report OWNER TO samplesvc;

--
-- Name: reportpkseq; Type: SEQUENCE; Schema: sample; Owner: samplesvc
--

CREATE SEQUENCE reportpkseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE reportpkseq OWNER TO samplesvc;

--
-- Name: reporttype; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE reporttype (
    reporttypepk character varying(20) NOT NULL,
    displayorder integer,
    displayname character varying(40)
);


ALTER TABLE reporttype OWNER TO samplesvc;

--
-- Name: samplesummary; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE samplesummary (
    samplesummarypk bigint NOT NULL,
    statefk character varying(20) NOT NULL,
    ingestdatetime timestamp with time zone,
    id uuid NOT NULL,
    description character varying(250),
    totalsampleunits integer,
    expectedcollectioninstruments integer
);


ALTER TABLE samplesummary OWNER TO samplesvc;

--
-- Name: samplesummaryseq; Type: SEQUENCE; Schema: sample; Owner: samplesvc
--

CREATE SEQUENCE samplesummaryseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE samplesummaryseq OWNER TO samplesvc;

--
-- Name: samplesummarystate; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE samplesummarystate (
    statepk character varying(20) NOT NULL
);


ALTER TABLE samplesummarystate OWNER TO samplesvc;

--
-- Name: sampleunit; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE sampleunit (
    sampleunitpk bigint NOT NULL,
    samplesummaryfk bigint NOT NULL,
    sampleunitref character varying(20),
    sampleunittype character varying(2),
    formtype character varying(10),
    statefk character varying(20) NOT NULL,
    id uuid NOT NULL
);


ALTER TABLE sampleunit OWNER TO samplesvc;

--
-- Name: sampleunitseq; Type: SEQUENCE; Schema: sample; Owner: samplesvc
--

CREATE SEQUENCE sampleunitseq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999999
    CACHE 1;


ALTER TABLE sampleunitseq OWNER TO samplesvc;

--
-- Name: sampleunitstate; Type: TABLE; Schema: sample; Owner: samplesvc
--

CREATE TABLE sampleunitstate (
    statepk character varying(20) NOT NULL
);


ALTER TABLE sampleunitstate OWNER TO samplesvc;

SET search_path = survey, pg_catalog;

--
-- Name: classifiertype; Type: TABLE; Schema: survey; Owner: postgres
--

CREATE TABLE classifiertype (
    classifiertypepk integer NOT NULL,
    classifiertypeselectorfk integer NOT NULL,
    classifiertype character varying(50) NOT NULL
);


ALTER TABLE classifiertype OWNER TO postgres;

--
-- Name: classifiertype_classifiertypepk_seq; Type: SEQUENCE; Schema: survey; Owner: postgres
--

CREATE SEQUENCE classifiertype_classifiertypepk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE classifiertype_classifiertypepk_seq OWNER TO postgres;

--
-- Name: classifiertype_classifiertypepk_seq; Type: SEQUENCE OWNED BY; Schema: survey; Owner: postgres
--

ALTER SEQUENCE classifiertype_classifiertypepk_seq OWNED BY classifiertype.classifiertypepk;


--
-- Name: classifiertypeselector; Type: TABLE; Schema: survey; Owner: postgres
--

CREATE TABLE classifiertypeselector (
    classifiertypeselectorpk integer NOT NULL,
    id uuid NOT NULL,
    surveyfk integer NOT NULL,
    classifiertypeselector character varying(50) NOT NULL
);


ALTER TABLE classifiertypeselector OWNER TO postgres;

--
-- Name: classifiertypeselector_classifiertypeselectorpk_seq; Type: SEQUENCE; Schema: survey; Owner: postgres
--

CREATE SEQUENCE classifiertypeselector_classifiertypeselectorpk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE classifiertypeselector_classifiertypeselectorpk_seq OWNER TO postgres;

--
-- Name: classifiertypeselector_classifiertypeselectorpk_seq; Type: SEQUENCE OWNED BY; Schema: survey; Owner: postgres
--

ALTER SEQUENCE classifiertypeselector_classifiertypeselectorpk_seq OWNED BY classifiertypeselector.classifiertypeselectorpk;


--
-- Name: survey; Type: TABLE; Schema: survey; Owner: postgres
--

CREATE TABLE survey (
    surveypk integer NOT NULL,
    id uuid NOT NULL,
    shortname character varying(20) NOT NULL,
    longname character varying(100) NOT NULL,
    surveyref character varying(20) NOT NULL,
    legalbasis character varying(400) NOT NULL
);


ALTER TABLE survey OWNER TO postgres;

--
-- Name: survey_surveypk_seq; Type: SEQUENCE; Schema: survey; Owner: postgres
--

CREATE SEQUENCE survey_surveypk_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE survey_surveypk_seq OWNER TO postgres;

--
-- Name: survey_surveypk_seq; Type: SEQUENCE OWNED BY; Schema: survey; Owner: postgres
--

ALTER SEQUENCE survey_surveypk_seq OWNED BY survey.surveypk;


SET search_path = templatesvc, pg_catalog;

--
-- Name: classificationtype; Type: TABLE; Schema: templatesvc; Owner: postgres
--

CREATE TABLE classificationtype (
    name text NOT NULL
);


ALTER TABLE classificationtype OWNER TO postgres;

--
-- Name: template; Type: TABLE; Schema: templatesvc; Owner: postgres
--

CREATE TABLE template (
    id uuid NOT NULL,
    label text,
    type public.communicationtype,
    uri text,
    classification jsonb,
    params jsonb
);


ALTER TABLE template OWNER TO postgres;

SET search_path = partysvc, pg_catalog;

--
-- Name: business_attributes id; Type: DEFAULT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business_attributes ALTER COLUMN id SET DEFAULT nextval('business_attributes_id_seq'::regclass);


--
-- Name: pending_enrolment id; Type: DEFAULT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY pending_enrolment ALTER COLUMN id SET DEFAULT nextval('pending_enrolment_id_seq'::regclass);


--
-- Name: respondent id; Type: DEFAULT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY respondent ALTER COLUMN id SET DEFAULT nextval('respondent_id_seq'::regclass);


SET search_path = public, pg_catalog;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: credentials_oauthclient id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY credentials_oauthclient ALTER COLUMN id SET DEFAULT nextval('credentials_oauthclient_id_seq'::regclass);


--
-- Name: credentials_oauthuser id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY credentials_oauthuser ALTER COLUMN id SET DEFAULT nextval('credentials_oauthuser_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: tokens_oauthaccesstoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken ALTER COLUMN id SET DEFAULT nextval('tokens_oauthaccesstoken_id_seq'::regclass);


--
-- Name: tokens_oauthaccesstoken_scopes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken_scopes ALTER COLUMN id SET DEFAULT nextval('tokens_oauthaccesstoken_scopes_id_seq'::regclass);


--
-- Name: tokens_oauthauthorizationcode id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode ALTER COLUMN id SET DEFAULT nextval('tokens_oauthauthorizationcode_id_seq'::regclass);


--
-- Name: tokens_oauthauthorizationcode_scopes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode_scopes ALTER COLUMN id SET DEFAULT nextval('tokens_oauthauthorizationcode_scopes_id_seq'::regclass);


--
-- Name: tokens_oauthrefreshtoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthrefreshtoken ALTER COLUMN id SET DEFAULT nextval('tokens_oauthrefreshtoken_id_seq'::regclass);


--
-- Name: tokens_oauthscope id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthscope ALTER COLUMN id SET DEFAULT nextval('tokens_oauthscope_id_seq'::regclass);


SET search_path = ras_ci, pg_catalog;

--
-- Name: business id; Type: DEFAULT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY business ALTER COLUMN id SET DEFAULT nextval('business_id_seq'::regclass);


--
-- Name: exercise id; Type: DEFAULT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY exercise ALTER COLUMN id SET DEFAULT nextval('exercise_id_seq'::regclass);


--
-- Name: instrument id; Type: DEFAULT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY instrument ALTER COLUMN id SET DEFAULT nextval('instrument_id_seq'::regclass);


--
-- Name: seft_instrument id; Type: DEFAULT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY seft_instrument ALTER COLUMN id SET DEFAULT nextval('seft_instrument_id_seq'::regclass);


--
-- Name: survey id; Type: DEFAULT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY survey ALTER COLUMN id SET DEFAULT nextval('survey_id_seq'::regclass);


SET search_path = survey, pg_catalog;

--
-- Name: classifiertype classifiertypepk; Type: DEFAULT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY classifiertype ALTER COLUMN classifiertypepk SET DEFAULT nextval('classifiertype_classifiertypepk_seq'::regclass);


--
-- Name: classifiertypeselector classifiertypeselectorpk; Type: DEFAULT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY classifiertypeselector ALTER COLUMN classifiertypeselectorpk SET DEFAULT nextval('classifiertypeselector_classifiertypeselectorpk_seq'::regclass);


--
-- Name: survey surveypk; Type: DEFAULT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY survey ALTER COLUMN surveypk SET DEFAULT nextval('survey_surveypk_seq'::regclass);


SET search_path = action, pg_catalog;

--
-- Data for Name: action; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY action (id, actionpk, caseid, casefk, actionplanfk, actionrulefk, actiontypefk, createdby, manuallycreated, priority, situation, statefk, createddatetime, updateddatetime, optlockversion) FROM stdin;
\.


--
-- Name: actionpkseq; Type: SEQUENCE SET; Schema: action; Owner: actionsvc
--

SELECT pg_catalog.setval('actionpkseq', 1, false);


--
-- Data for Name: actionplan; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY actionplan (id, actionplanpk, name, description, createdby, lastrundatetime) FROM stdin;
0009e978-0932-463b-a2a1-b45cb3ffcb2a	2	Reminder	BRES	SYSTEM	\N
e71002ac-3575-47eb-b87f-cd9db92bf9a7	1	Notification	BRES Enrolment	SYSTEM	\N
\.


--
-- Data for Name: actionplanjob; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY actionplanjob (id, actionplanjobpk, actionplanfk, createdby, statefk, createddatetime, updateddatetime) FROM stdin;
\.


--
-- Name: actionplanjobseq; Type: SEQUENCE SET; Schema: action; Owner: actionsvc
--

SELECT pg_catalog.setval('actionplanjobseq', 1, false);


--
-- Data for Name: actionplanjobstate; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY actionplanjobstate (statepk) FROM stdin;
SUBMITTED
STARTED
COMPLETED
FAILED
\.


--
-- Data for Name: actionrule; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY actionrule (actionrulepk, actionplanfk, actiontypefk, name, description, daysoffset, priority) FROM stdin;
2	1	2	BSREM+45	Enrolment Reminder Letter(+45 days)	45	3
3	1	2	BSREM+73	Enrolment Reminder Letter(+73 days)	73	3
4	2	3	BSSNE+45	Survey Reminder Notification(+45 days)	45	3
5	2	3	BSSNE+73	Survey Reminder Notification(+73 days)	73	3
1	1	1	BSNOT+0	Enrolment Invitation Letter(+0 days)	0	3
\.


--
-- Data for Name: actionstate; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY actionstate (statepk) FROM stdin;
SUBMITTED
PENDING
ACTIVE
COMPLETED
CANCEL_SUBMITTED
CANCELLED
CANCEL_PENDING
CANCELLING
ABORTED
\.


--
-- Data for Name: actiontype; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY actiontype (actiontypepk, name, description, handler, cancancel, responserequired) FROM stdin;
1	BSNOT	Enrolment Invitation Letter	Printer	f	f
2	BSREM	Enrolment Reminder Letter	Printer	f	f
3	BSSNE	Survey Reminder Notification	Notify	f	f
\.


--
-- Data for Name: case; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY "case" (actionplanid, id, casepk, actionplanfk, actionplanstartdate, actionplanenddate) FROM stdin;
\.


--
-- Name: casepkseq; Type: SEQUENCE SET; Schema: action; Owner: actionsvc
--

SELECT pg_catalog.setval('casepkseq', 1, false);


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
10.37.0-1	Sarah Radford	database/changes/release-10.37.0/changelog.yml	2018-03-08 15:32:01.161719	1	EXECUTED	7:0e71e8d5f1af547c54ea8a21cebb00a1	sqlFile		\N	3.5.3	\N	\N	0523120685
10.37.0-2	Sarah Radford	database/changes/release-10.37.0/changelog.yml	2018-03-08 15:32:01.27163	2	EXECUTED	7:0cf5d77081b31f353e16b69b644fea25	sqlFile		\N	3.5.3	\N	\N	0523120685
10.43.0-1	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:32:01.360994	3	EXECUTED	7:6956f3628325483fbbebbb3f21316c9a	sqlFile		\N	3.5.3	\N	\N	0523120685
10.43.0-2	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:32:01.536717	4	EXECUTED	7:85891b5dabf7d7a8568036a380196ba8	sqlFile		\N	3.5.3	\N	\N	0523120685
10.45.0-1	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:32:01.742064	5	EXECUTED	7:975a9ad06bb1327ca0a7c7597fce13e5	sqlFile		\N	3.5.3	\N	\N	0523120685
10.46.0-1	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:32:01.803174	6	EXECUTED	7:80e723c587adb6612b6a8c73f4f2d88a	sqlFile		\N	3.5.3	\N	\N	0523120685
10.46.0-2	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:32:01.839665	7	EXECUTED	7:a56dffa5ccfc08188c90e103c9f38020	sqlFile		\N	3.5.3	\N	\N	0523120685
10.46.0-3	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:32:01.912943	8	EXECUTED	7:3cf299ad6c4949aaa578788ce17c1608	sqlFile		\N	3.5.3	\N	\N	0523120685
10.46.0-4	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:32:01.946667	9	EXECUTED	7:2197f7c617038235be1c575fcdf2268e	sqlFile		\N	3.5.3	\N	\N	0523120685
10.47.0-1	Sarah Radford	database/changes/release-10.47.0/changelog.yml	2018-03-08 15:32:02.01191	10	EXECUTED	7:954ae53fc16c2226221fbdaffbd52416	sqlFile		\N	3.5.3	\N	\N	0523120685
10.47.0-2	Sarah Radford	database/changes/release-10.47.0/changelog.yml	2018-03-08 15:32:02.03272	11	EXECUTED	7:860a5372283b07eae1199d50ad526fdc	sqlFile		\N	3.5.3	\N	\N	0523120685
10.49.0-1	Tejas Patel	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:32:02.04797	12	EXECUTED	7:1eb9fe94896a0b075a9b6ed5318c117e	sqlFile		\N	3.5.3	\N	\N	0523120685
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: messagelog; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY messagelog (messagepk, messagetext, jobid, messagelevel, functionname, createddatetime) FROM stdin;
1	GENERATING ACTION MI REPORT	0	INFO	action.generate_action_mi	2018-03-08 15:34:00.217339+00
2	GENERATING ACTIONS MI REPORT COMPLETED ROWS WRIITEN = 5	0	INFO	action.generate_action_mi	2018-03-08 15:34:00.217339+00
3	ACTIONS MI REPORT GENERATED	0	INFO	action.generate_action_mi	2018-03-08 15:34:00.217339+00
4	GENERATING ACTION MI REPORT	0	INFO	action.generate_action_mi	2018-03-08 15:35:00.014218+00
5	GENERATING ACTIONS MI REPORT COMPLETED ROWS WRIITEN = 5	0	INFO	action.generate_action_mi	2018-03-08 15:35:00.014218+00
6	ACTIONS MI REPORT GENERATED	0	INFO	action.generate_action_mi	2018-03-08 15:35:00.014218+00
\.


--
-- Name: messageseq; Type: SEQUENCE SET; Schema: action; Owner: actionsvc
--

SELECT pg_catalog.setval('messageseq', 6, true);


--
-- Data for Name: outcomecategory; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY outcomecategory (handlerpk, actionoutcomepk, eventcategory) FROM stdin;
Field	REQUEST_COMPLETED	ACTION_COMPLETED
Field	REQUEST_COMPLETED_DEACTIVATE	ACTION_COMPLETED_DEACTIVATED
Field	REQUEST_COMPLETED_DISABLE	ACTION_COMPLETED_DISABLED
Notify	REQUEST_COMPLETED	ACTION_COMPLETED
Notify	REQUEST_COMPLETED_DEACTIVATE	ACTION_COMPLETED_DEACTIVATED
Notify	REQUEST_COMPLETED_DISABLE	ACTION_COMPLETED_DISABLED
Printer	REQUEST_COMPLETED	ACTION_COMPLETED
Printer	REQUEST_COMPLETED_DEACTIVATE	ACTION_COMPLETED_DEACTIVATED
Printer	REQUEST_COMPLETED_DISABLE	ACTION_COMPLETED_DISABLED
\.


--
-- Data for Name: report; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY report (id, reportpk, reporttypefk, contents, createddatetime) FROM stdin;
98340e06-38de-495a-b53c-4ce42bde944b	1	ACTIONS	Action Plan No,Action Plan Name,Action Type,Action Plan Start Date,Days Offset,Handler,Count,State\n1,BRES Enrolment,Enrolment Invitation Letter,,0,Printer,0,\n1,BRES Enrolment,Enrolment Reminder Letter,,45,Printer,0,\n1,BRES Enrolment,Enrolment Reminder Letter,,73,Printer,0,\n2,BRES,Survey Reminder Notification,,45,Notify,0,\n2,BRES,Survey Reminder Notification,,73,Notify,0,	2018-03-08 15:34:00.217339+00
c4d213a0-769e-4ffd-bff0-15cd4b1513fc	2	ACTIONS	Action Plan No,Action Plan Name,Action Type,Action Plan Start Date,Days Offset,Handler,Count,State\n1,BRES Enrolment,Enrolment Invitation Letter,,0,Printer,0,\n1,BRES Enrolment,Enrolment Reminder Letter,,45,Printer,0,\n1,BRES Enrolment,Enrolment Reminder Letter,,73,Printer,0,\n2,BRES,Survey Reminder Notification,,45,Notify,0,\n2,BRES,Survey Reminder Notification,,73,Notify,0,	2018-03-08 15:35:00.014218+00
\.


--
-- Name: reportpkseq; Type: SEQUENCE SET; Schema: action; Owner: actionsvc
--

SELECT pg_catalog.setval('reportpkseq', 2, true);


--
-- Data for Name: reporttype; Type: TABLE DATA; Schema: action; Owner: actionsvc
--

COPY reporttype (reporttypepk, displayorder, displayname) FROM stdin;
ACTIONS	10	Action Status
\.


SET search_path = actionexporter, pg_catalog;

--
-- Data for Name: actionrequest; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY actionrequest (actionrequestpk, actionid, responserequired, actionplanname, actiontypename, questionset, contactfk, sampleunitreffk, caseid, priority, caseref, iac, datestored, datesent, exerciseref, legalbasis, region, respondentstatus, enrolmentstatus, casegroupstatus, surveyref) FROM stdin;
\.


--
-- Name: actionrequestpkseq; Type: SEQUENCE SET; Schema: actionexporter; Owner: actionexportersvc
--

SELECT pg_catalog.setval('actionrequestpkseq', 1, false);


--
-- Data for Name: address; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY address (sampleunitrefpk, addresstype, estabtype, category, organisation_name, address_line1, address_line2, locality, town_name, postcode, lad, latitude, longitude) FROM stdin;
\.


--
-- Data for Name: contact; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY contact (contactpk, forename, surname, phonenumber, emailaddress, title) FROM stdin;
\.


--
-- Name: contactpkseq; Type: SEQUENCE SET; Schema: actionexporter; Owner: actionexportersvc
--

SELECT pg_catalog.setval('contactpkseq', 1, false);


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
10.40.0-1	Sarah Radford	database/changes/release-10.40.0/changelog.yml	2018-03-08 15:31:06.937322	1	EXECUTED	7:4011253ef9c5f1bcda7b26e8eec00c93	sqlFile		\N	3.5.3	\N	\N	0523066524
10.40.0-2	Sarah Radford	database/changes/release-10.40.0/changelog.yml	2018-03-08 15:31:06.988866	2	EXECUTED	7:2d95c060681c9dbf5bd070606ce25c13	sqlFile		\N	3.5.3	\N	\N	0523066524
10.43.0-1	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:07.050071	3	EXECUTED	7:a664ae020b2cee750a63c94ff09de3e5	sqlFile		\N	3.5.3	\N	\N	0523066524
10.43.0-2	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:07.182115	4	EXECUTED	7:cdf416190829d7d6f55e35fdf876624c	sqlFile		\N	3.5.3	\N	\N	0523066524
10.43.0-3	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:07.202609	5	EXECUTED	7:096deb4597fd60aaa2fca5c33e5eb596	sqlFile		\N	3.5.3	\N	\N	0523066524
10.43.0-4	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:07.230166	6	EXECUTED	7:9eed897d2d3d734f419c711fef9e4e5b	sqlFile		\N	3.5.3	\N	\N	0523066524
10.44.0-1	Gareth Turner	database/changes/release-10.44.0/changelog.yml	2018-03-08 15:31:07.259493	7	EXECUTED	7:9eed897d2d3d734f419c711fef9e4e5b	sqlFile		\N	3.5.3	\N	\N	0523066524
10.44.0-2	Chris Hardman	database/changes/release-10.44.0/changelog.yml	2018-03-08 15:31:07.301828	8	EXECUTED	7:31f1f65436cbcdd41fdb34b406bcdadc	sqlFile		\N	3.5.3	\N	\N	0523066524
10.44.0-3	Kieran Wardle	database/changes/release-10.44.0/changelog.yml	2018-03-08 15:31:07.323582	9	EXECUTED	7:e310a673b006a9c85a1b1d5bc7bfbfb8	sqlFile		\N	3.5.3	\N	\N	0523066524
10.45.0-1	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:07.393675	10	EXECUTED	7:b68536b0d7a018c9062198d600568d1e	sqlFile		\N	3.5.3	\N	\N	0523066524
10.45.0-2	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:07.412676	11	EXECUTED	7:35b6de9efbf79615f1165c68068c449b	sqlFile		\N	3.5.3	\N	\N	0523066524
10.47.0-1	Edward Stevens	database/changes/release-10.47.0/changelog.yml	2018-03-08 15:31:07.458432	12	EXECUTED	7:f8d92d734264ccacef0f6e681d9b592b	sqlFile		\N	3.5.3	\N	\N	0523066524
10.49.0	Richard Weeks	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:31:07.484403	13	EXECUTED	7:6196ceabacc1905847f4291621cff684	sqlFile		\N	3.5.3	\N	\N	0523066524
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: filerowcount; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY filerowcount (filename, rowcount, datesent, reported, sendresult) FROM stdin;
\.


--
-- Data for Name: messagelog; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY messagelog (messagepk, messagetext, jobid, messagelevel, functionname, createddatetime) FROM stdin;
1	GENERATING PRINT VOLUMES MI REPORT	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:33:00.442835+00
2	GENERATING PRINT VOLUMES MI REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:33:00.442835+00
3	PRINT VOLUMES MI REPORT GENERATED	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:33:00.442835+00
4	GENERATING PRINT VOLUMES MI REPORT	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:34:00.0782+00
5	GENERATING PRINT VOLUMES MI REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:34:00.0782+00
6	PRINT VOLUMES MI REPORT GENERATED	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:34:00.0782+00
7	GENERATING PRINT VOLUMES MI REPORT	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:35:00.08154+00
8	GENERATING PRINT VOLUMES MI REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:35:00.08154+00
9	PRINT VOLUMES MI REPORT GENERATED	0	INFO	actionexporter.generate_print_volumes_mi	2018-03-08 15:35:00.08154+00
\.


--
-- Name: messageseq; Type: SEQUENCE SET; Schema: actionexporter; Owner: actionexportersvc
--

SELECT pg_catalog.setval('messageseq', 9, true);


--
-- Data for Name: report; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY report (id, reportpk, reporttypefk, contents, createddatetime) FROM stdin;
\.


--
-- Name: reportpkseq; Type: SEQUENCE SET; Schema: actionexporter; Owner: actionexportersvc
--

SELECT pg_catalog.setval('reportpkseq', 1, false);


--
-- Data for Name: reporttype; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY reporttype (reporttypepk, displayorder, displayname) FROM stdin;
PRINT_VOLUMES	10	Print Volumes
\.


--
-- Data for Name: template; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY template (templatenamepk, content, datemodified) FROM stdin;
initialPrint	<#list actionRequests as actionRequest>\n${(actionRequest.address.sampleUnitRef?trim)!}:${actionRequest.iac?trim}:${(actionRequest.contact.forename?trim)!"null"}:${(actionRequest.contact.emailAddress)!"null"}\n  </#list>	2018-03-08 15:31:06.96728+00
\.


--
-- Data for Name: templatemapping; Type: TABLE DATA; Schema: actionexporter; Owner: actionexportersvc
--

COPY templatemapping (actiontypenamepk, templatenamefk, filenameprefix, datemodified) FROM stdin;
BSNOT	initialPrint	BSNOT	2018-03-08 15:31:06.96728+00
BSREM	initialPrint	BSREM	2018-03-08 15:31:06.96728+00
\.


SET search_path = casesvc, pg_catalog;

--
-- Data for Name: case; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY "case" (casepk, id, caseref, casegroupfk, casegroupid, partyid, sampleunittype, collectioninstrumentid, statefk, actionplanid, createddatetime, createdby, iac, sourcecase, optlockversion) FROM stdin;
\.


--
-- Data for Name: caseevent; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY caseevent (caseeventpk, casefk, description, createdby, createddatetime, categoryfk, subcategory) FROM stdin;
\.


--
-- Name: caseeventseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('caseeventseq', 1, false);


--
-- Data for Name: casegroup; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY casegroup (casegrouppk, id, partyid, collectionexerciseid, sampleunitref, sampleunittype, status) FROM stdin;
\.


--
-- Name: casegroupseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('casegroupseq', 1, false);


--
-- Data for Name: casegroupstatusaudit; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY casegroupstatusaudit (casegroupstatusauditpk, casegroupfk, partyid, status, createddatetime) FROM stdin;
\.


--
-- Name: casegroupstatusauditseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('casegroupstatusauditseq', 1, false);


--
-- Name: caserefseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('caserefseq', 1000000000000001, false);


--
-- Name: caseseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('caseseq', 1, false);


--
-- Data for Name: casestate; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY casestate (statepk) FROM stdin;
ACTIONABLE
INACTIONABLE
REPLACEMENT_INIT
SAMPLED_INIT
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY category (categorypk, shortdescription, longdescription, eventtype, role, generatedactiontype, "group", oldcasesampleunittypes, newcasesampleunittype, recalccollectioninstrument) FROM stdin;
ACTION_CREATED	Action Created	Action Created	\N	\N	\N	\N	B,BI	\N	\N
ACTION_COMPLETED	Action Completed	Action Completed	\N	\N	\N	\N	B,BI	\N	\N
ACTION_UPDATED	Action Updated	Action Updated	\N	\N	\N	\N	B,BI	\N	\N
CASE_CREATED	Case Created	Case Created	\N	\N	\N	\N	B,BI	\N	\N
RESPONDENT_ACCOUNT_CREATED	Account created for respondent	Account created for respondent	ACCOUNT_CREATED	\N	\N	\N	B	\N	\N
ACCESS_CODE_AUTHENTICATION_ATTEMPT	Access Code authentication attempted	Access Code authentication attempted	\N	\N	\N	\N	B	\N	\N
COLLECTION_INSTRUMENT_DOWNLOADED	Collection Instrument Downloaded	Collection Instrument Downloaded	\N	\N	\N	\N	BI	\N	\N
ACTION_CANCELLATION_COMPLETED	Action Cancellation Completed	Action Cancellation Completed	\N	\N	\N	\N	B,BI	\N	\N
ACTION_CANCELLATION_CREATED	Action Cancellation Created	Action Cancellation Created	\N	\N	\N	\N	B,BI	\N	\N
UNSUCCESSFUL_RESPONSE_UPLOAD	Unsuccessful Response Upload	Unsuccessful Response Upload	\N	\N	\N	\N	BI	\N	\N
SUCCESSFUL_RESPONSE_UPLOAD	Successful Response Upload	Successful Response Upload	DISABLED	\N	\N	\N	BI	\N	\N
RESPONDENT_ENROLED	Respondent Enroled	Respondent Enroled	DEACTIVATED	\N	\N	\N	B	BI	\N
SECURE_MESSAGE_SENT	Secure Message Sent	Secure Message Sent	\N	\N	\N	\N	BI	\N	\N
COLLECTION_INSTRUMENT_ERROR	Collection Instrument Error	Collection Instrument Error	\N	\N	\N	\N	BI	\N	\N
VERIFICATION_CODE_SENT	Verification Code Sent	Verification Code Sent	\N	\N	\N	\N	B	\N	\N
RESPONDENT_EMAIL_AMENDED	Respondent Email Amended	Respondent Email Amended	\N	\N	\N	\N	BI	\N	\N
OFFLINE_RESPONSE_PROCESSED	Offline Response Processed	Offline Response Processed	DISABLED	\N	\N	\N	BI	\N	\N
COMPLETED_BY_PHONE	Completed By Phone	Completed By Phone	DEACTIVATED	\N	\N	\N	B,BI	\N	\N
EQ_LAUNCH	Collection Instrument Launched	Collection Instrument Launched	\N	\N	\N	\N	BI	\N	\N
\.


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
10.39.0-1	Narinder Birk	database/changes/release-10.39.0/changelog.yml	2018-03-08 15:31:12.618707	1	EXECUTED	7:7f8e03d0f3252510f904d7444bfeebd0	sqlFile		\N	3.5.3	\N	\N	0523071836
10.39.0-2	Narinder Birk	database/changes/release-10.39.0/changelog.yml	2018-03-08 15:31:12.757904	2	EXECUTED	7:13ccf33122d43460953e0cdfce0d9eec	sqlFile		\N	3.5.3	\N	\N	0523071836
10.39.0-3	Narinder Birk	database/changes/release-10.39.0/changelog.yml	2018-03-08 15:31:12.815526	3	EXECUTED	7:df584fd38c4d8a1f568a6fb5fceddecd	sqlFile		\N	3.5.3	\N	\N	0523071836
10.40.0-1	Narinder Birk	database/changes/release-10.40.0/changelog.yml	2018-03-08 15:31:12.864556	4	EXECUTED	7:f4ccba8089aa4311c5999d0fcbf91be2	sqlFile		\N	3.5.3	\N	\N	0523071836
10.41.0-1	Narinder Birk	database/changes/release-10.41.0/changelog.yml	2018-03-08 15:31:12.952416	5	EXECUTED	7:1b04d959836a5717d06113ed862cae98	sqlFile		\N	3.5.3	\N	\N	0523071836
10.43.0-1	Narinder Birk	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:13.272637	6	EXECUTED	7:8be3cf75eb8e0005dcaf8fb17b16a574	sqlFile		\N	3.5.3	\N	\N	0523071836
10.43.0-2	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:13.510815	7	EXECUTED	7:8ac8601c02c9167ddb06b02ba7a3715e	sqlFile		\N	3.5.3	\N	\N	0523071836
10.44.0-1	Sarah Radford	database/changes/release-10.44.0/changelog.yml	2018-03-08 15:31:13.543026	8	EXECUTED	7:edf90b6d72362e083f6f9a16c822a31d	sqlFile		\N	3.5.3	\N	\N	0523071836
10.44.0-2	John Topley	database/changes/release-10.44.0/changelog.yml	2018-03-08 15:31:13.587743	9	EXECUTED	7:6dbbfb7d1a01a64f38a57946c6f985a6	sqlFile		\N	3.5.3	\N	\N	0523071836
10.44.0-3	Edward Stevens	database/changes/release-10.44.0/changelog.yml	2018-03-08 15:31:13.670375	10	EXECUTED	7:8c967460d5ca726f76da82dcd267419d	sqlFile		\N	3.5.3	\N	\N	0523071836
10.45.0-1	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:13.770666	11	EXECUTED	7:07e819834538fc465127f6fb5bfa1943	sqlFile		\N	3.5.3	\N	\N	0523071836
10.45.0-2	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:13.842919	12	EXECUTED	7:f5adf13c866a3d60b58bedbb2eafdcff	sqlFile		\N	3.5.3	\N	\N	0523071836
10.45.0-3	Edward Stevens	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:13.908457	13	EXECUTED	7:e51ec38d701d3e31ccf3ff49d7862cb5	sqlFile		\N	3.5.3	\N	\N	0523071836
10.45.0-4	Edward Stevens	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:13.9573	14	EXECUTED	7:35ca614d15a2a1a72d4c465af77c3379	sqlFile		\N	3.5.3	\N	\N	0523071836
10.46.0-1	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:31:14.056817	15	EXECUTED	7:4544b25cc9744c7a628293367b66e7f7	sqlFile		\N	3.5.3	\N	\N	0523071836
10.46.0-2	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:31:14.160285	16	EXECUTED	7:5cfcd1a95b4b207490198ccad042385a	sqlFile		\N	3.5.3	\N	\N	0523071836
10.46.0-3	Chris Hardman	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:31:14.166098	17	EXECUTED	7:203a13a8a0dbd0cf735e4a83503d95ba	sqlFile		\N	3.5.3	\N	\N	0523071836
10.47.0-1	Narinder Birk	database/changes/release-10.47.0/changelog.yml	2018-03-08 15:31:14.171297	18	EXECUTED	7:c19a17686ea126affe7c93d7a74e1a10	sqlFile		\N	3.5.3	\N	\N	0523071836
10.47.0-2	Narinder Birk	database/changes/release-10.47.0/changelog.yml	2018-03-08 15:31:14.195161	19	EXECUTED	7:8d3b3a72f681d130ca09f097fe6c9e0f	sqlFile		\N	3.5.3	\N	\N	0523071836
10.49.0-1	Joe Walton	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:31:14.212776	20	EXECUTED	7:3edb8fede35188cdd7ab9c2ba3f3acbf	sqlFile		\N	3.5.3	\N	\N	0523071836
10.50.0-1	Joe Walton	database/changes/release-10.50.0/changelog.yml	2018-03-08 15:31:14.249456	21	EXECUTED	7:54bbf471299dd378c56da0833036e92e	sqlFile		\N	3.5.3	\N	\N	0523071836
10.51.0-1	Lewis Babbage	database/changes/release-10.51.0/changelog.yml	2018-03-08 15:31:14.271092	22	EXECUTED	7:8373fe9df6ad71d6bc916ed7220a720c	sqlFile		\N	3.5.3	\N	\N	0523071836
10.52.0-1	Joe Walton	database/changes/release-10.52.0/changelog.yml	2018-03-08 15:31:14.290776	23	EXECUTED	7:7f0bcefcdcc9777521362e6e4f8e0166	sqlFile		\N	3.5.3	\N	\N	0523071836
10.52.0-2	Ben Jefferies	database/changes/release-10.52.0/changelog.yml	2018-03-08 15:31:14.297583	24	EXECUTED	7:f5e8875b2e8e5dee907e54af8acb2a76	sqlFile		\N	3.5.3	\N	\N	0523071836
10.52.0-3	Tejas Patel	database/changes/release-10.52.0/changelog.yml	2018-03-08 15:31:14.325739	25	EXECUTED	7:e655c80608f1503fd35873f3001e1d36	sqlFile		\N	3.5.3	\N	\N	0523071836
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: messagelog; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY messagelog (messagelogpk, messagetext, jobid, messagelevel, functionname, createddatetime) FROM stdin;
1	GENERATING RESPONSE CHASING REPORT	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:33:00.146296+00
2	GENERATING RESPONSE CHASING REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:33:00.146296+00
3	RESPONSE CHASING REPORT GENERATED	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:33:00.146296+00
4	GENERATING CASE EVENTS REPORT	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:33:00.168172+00
5	GENERATING CASE EVENTS REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:33:00.168172+00
6	CASE EVENTS REPORT GENERATED	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:33:00.168172+00
7	GENERATING RESPONSE CHASING REPORT	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:34:00.017896+00
8	GENERATING RESPONSE CHASING REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:34:00.017896+00
9	RESPONSE CHASING REPORT GENERATED	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:34:00.017896+00
10	GENERATING CASE EVENTS REPORT	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:34:00.028133+00
11	GENERATING CASE EVENTS REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:34:00.028133+00
12	CASE EVENTS REPORT GENERATED	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:34:00.028133+00
13	GENERATING RESPONSE CHASING REPORT	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:35:00.01789+00
14	GENERATING RESPONSE CHASING REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:35:00.01789+00
15	RESPONSE CHASING REPORT GENERATED	0	INFO	casesvc.generate_response_chasing_report	2018-03-08 15:35:00.01789+00
16	GENERATING CASE EVENTS REPORT	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:35:00.021307+00
17	GENERATING CASE EVENTS REPORT COMPLETED ROWS WRIITEN = 0	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:35:00.021307+00
18	CASE EVENTS REPORT GENERATED	0	INFO	casesvc.generate_case_events_report	2018-03-08 15:35:00.021307+00
\.


--
-- Name: messagelogseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('messagelogseq', 18, true);


--
-- Data for Name: report; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY report (id, reportpk, reporttypefk, contents, createddatetime) FROM stdin;
\.


--
-- Name: reportpkseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('reportpkseq', 1, false);


--
-- Data for Name: reporttype; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY reporttype (reporttypepk, displayorder, displayname) FROM stdin;
CASE_EVENTS	1	Case Events
RESPONSE_CHASING	2	Response Chasing
\.


--
-- Data for Name: response; Type: TABLE DATA; Schema: casesvc; Owner: casesvc
--

COPY response (responsepk, casefk, inboundchannel, responsedatetime) FROM stdin;
\.


--
-- Name: responseseq; Type: SEQUENCE SET; Schema: casesvc; Owner: casesvc
--

SELECT pg_catalog.setval('responseseq', 1, false);


SET search_path = collectionexercise, pg_catalog;

--
-- Data for Name: casetypedefault; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY casetypedefault (casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid) FROM stdin;
2	BI	0009e978-0932-463b-a2a1-b45cb3ffcb2a	cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87
1	B	e71002ac-3575-47eb-b87f-cd9db92bf9a7	cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87
\.


--
-- Data for Name: casetypeoverride; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY casetypeoverride (casetypeoverridepk, exercisefk, sampleunittypefk, actionplanid) FROM stdin;
\.


--
-- Data for Name: collectionexercise; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY collectionexercise (id, exercisepk, name, scheduledstartdatetime, scheduledexecutiondatetime, scheduledreturndatetime, scheduledenddatetime, periodstartdatetime, periodenddatetime, actualexecutiondatetime, actualpublishdatetime, executedby, statefk, samplesize, exerciseref, user_description, created, updated, deleted, survey_uuid) FROM stdin;
14fb3e68-4dca-46db-bf49-04b84e07e77c	1	BRES_2017	2017-09-11 23:00:00+00	2017-09-10 23:00:00+00	2017-10-06 00:00:00+00	2018-06-29 23:00:00+00	2017-09-14 23:00:00+00	2017-09-15 22:59:59+00	\N	\N	\N	CREATED	\N	221_201712	\N	\N	\N	f	cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87
\.


--
-- Data for Name: collectionexercisestate; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY collectionexercisestate (statepk) FROM stdin;
EXECUTED
VALIDATED
FAILEDVALIDATION
SCHEDULED
READY_FOR_REVIEW
READY_FOR_LIVE
CREATED
EXECUTION_STARTED
LIVE
\.


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
10.37.0-1	Sarah Radford	database/changes/release-10.37.0/changelog.yml	2018-03-08 15:31:41.25879	1	EXECUTED	7:4ac699ca18a5b1d347bdeb46b0a0c651	sqlFile		\N	3.5.3	\N	\N	0523100877
10.37.0-2	Sarah Radford	database/changes/release-10.37.0/changelog.yml	2018-03-08 15:31:41.346322	2	EXECUTED	7:3bfc1e2399f2c7ef12769fdd64dc2dcb	sqlFile		\N	3.5.3	\N	\N	0523100877
10.43.0-1	Sarah Radford	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:41.403922	3	EXECUTED	7:b804f90e987fa3a94420a9b576d6bc28	sqlFile		\N	3.5.3	\N	\N	0523100877
10.45.0-1	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:41.470734	4	EXECUTED	7:23ed22bfb3addaac8dcee120fef357d3	sqlFile		\N	3.5.3	\N	\N	0523100877
10.45.0-2	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:41.564824	5	EXECUTED	7:350228b97709e691eb2b6a9b82d5a70a	sqlFile		\N	3.5.3	\N	\N	0523100877
10.46.0-1	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:31:41.699513	6	EXECUTED	7:84602ef424c9e68227a7f844ff851923	sqlFile		\N	3.5.3	\N	\N	0523100877
10.46.0-2	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:31:41.733526	7	EXECUTED	7:62e9f91262ba368e00141464c0f68ffd	sqlFile		\N	3.5.3	\N	\N	0523100877
10.47.0-1	Sarah Radford	database/changes/release-10.47.0/changelog.yml	2018-03-08 15:31:41.774221	8	EXECUTED	7:559b09db76c3cf619829b2742dbcc924	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.0-1	Sarah Radford	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:31:41.791829	9	EXECUTED	7:edbfc38b1a5692428c929fc1f6a0bf7c	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.0-2	Sarah Radford	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:31:41.847726	10	EXECUTED	7:bbc7191cfc976e0c5f0f1445b2617c9a	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-1	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:41.924377	11	EXECUTED	7:35f7062dd766e5e562313fec205f6c94	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-2	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:41.9763	12	EXECUTED	7:c4ed90695ab3670acea93e6e555f62a9	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-3	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.019582	13	EXECUTED	7:a5197d092046c26bba9ab7cda9982dc2	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-4	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.074441	14	EXECUTED	7:507075bfd5755927e66a6bffd55e8070	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-5	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.142174	15	EXECUTED	7:b19a8c7d6908f7a318fe2400b63d9e33	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-6	Ben Jefferies	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.192939	16	EXECUTED	7:88d1097628dbd36891f99ae7dd6fe85e	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-7	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.233054	17	EXECUTED	7:bffc4dfee2f6712e1b9fcdb8cfdb6b3d	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-8	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.280732	18	EXECUTED	7:53f129b6282b1de366428d970cb1d72a	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-9	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.295814	19	EXECUTED	7:6590cf99d44e826d74e6b3c991323ec8	sqlFile		\N	3.5.3	\N	\N	0523100877
10.49.2-10	Matt Innes	database/changes/release-10.49.2/changelog.yml	2018-03-08 15:31:42.365497	20	EXECUTED	7:cdadf362770fe542fe3fffc5f781e643	sqlFile		\N	3.5.3	\N	\N	0523100877
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY event (id, eventpk, collexfk, tag, "timestamp", created, updated, deleted, message_sent) FROM stdin;
\.


--
-- Name: eventpkseq; Type: SEQUENCE SET; Schema: collectionexercise; Owner: collectionexercisesvc
--

SELECT pg_catalog.setval('eventpkseq', 1, false);


--
-- Name: exercisepkseq; Type: SEQUENCE SET; Schema: collectionexercise; Owner: collectionexercisesvc
--

SELECT pg_catalog.setval('exercisepkseq', 4, true);


--
-- Data for Name: messagelog; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY messagelog (messagelogpk, messagetext, jobid, messagelevel, functionname, createddatetime) FROM stdin;
\.


--
-- Name: messagelogseq; Type: SEQUENCE SET; Schema: collectionexercise; Owner: collectionexercisesvc
--

SELECT pg_catalog.setval('messagelogseq', 1, false);


--
-- Data for Name: report; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY report (id, reportpk, reporttypefk, contents, createddatetime) FROM stdin;
\.


--
-- Name: reportpkseq; Type: SEQUENCE SET; Schema: collectionexercise; Owner: collectionexercisesvc
--

SELECT pg_catalog.setval('reportpkseq', 1, false);


--
-- Data for Name: reporttype; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY reporttype (reporttypepk, displayorder, displayname) FROM stdin;
COLLECTIONEXERCISE	30	Collection Exercise
\.


--
-- Data for Name: samplelink; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY samplelink (collectionexerciseid, samplesummaryid, samplelinkpk) FROM stdin;
\.


--
-- Name: samplelinkpkseq; Type: SEQUENCE SET; Schema: collectionexercise; Owner: collectionexercisesvc
--

SELECT pg_catalog.setval('samplelinkpkseq', 1, false);


--
-- Data for Name: sampleunit; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY sampleunit (sampleunitpk, sampleunitgroupfk, collectioninstrumentid, partyid, sampleunitref, sampleunittypefk) FROM stdin;
\.


--
-- Data for Name: sampleunitgroup; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY sampleunitgroup (sampleunitgrouppk, exercisefk, formtype, statefk, createddatetime, modifieddatetime) FROM stdin;
\.


--
-- Name: sampleunitgrouppkseq; Type: SEQUENCE SET; Schema: collectionexercise; Owner: collectionexercisesvc
--

SELECT pg_catalog.setval('sampleunitgrouppkseq', 1, false);


--
-- Data for Name: sampleunitgroupstate; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY sampleunitgroupstate (statepk) FROM stdin;
INIT
EXECUTED
VALIDATED
PUBLISHED
FAILEDVALIDATION
\.


--
-- Name: sampleunitpkseq; Type: SEQUENCE SET; Schema: collectionexercise; Owner: collectionexercisesvc
--

SELECT pg_catalog.setval('sampleunitpkseq', 1, false);


--
-- Data for Name: sampleunittype; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY sampleunittype (sampleunittypepk) FROM stdin;
B
BI
\.


--
-- Data for Name: survey; Type: TABLE DATA; Schema: collectionexercise; Owner: collectionexercisesvc
--

COPY survey (id, surveypk, surveyref) FROM stdin;
cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87	1	221
\.


SET search_path = iac, pg_catalog;

--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: iac; Owner: postgres
--

COPY databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
9.23.0-1	John Topley	database/changes/release-9.23.0/changelog.yml	2018-03-08 15:31:03.26108	1	EXECUTED	7:8aed45266de0f94932cdd9006defdd9f	sqlFile		\N	3.5.3	\N	\N	0523063085
9.30.0-1	John Topley	database/changes/release-9.30.1/changelog.yml	2018-03-08 15:31:03.420406	2	EXECUTED	7:c74d320bcd79ec9971836f7e0a5315e2	sqlFile		\N	3.5.3	\N	\N	0523063085
9.31.0-1	Chris Hardman, Edward Stevens	database/changes/release-9.31.0/changelog.yml	2018-03-08 15:31:03.453299	3	EXECUTED	7:ad49eb823e17bae300f0c60e5945f6b6	sqlFile		\N	3.5.3	\N	\N	0523063085
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: iac; Owner: postgres
--

COPY databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: iac; Type: TABLE DATA; Schema: iac; Owner: postgres
--

COPY iac (code, active, createddatetime, createdby, updateddatetime, updatedby, lastuseddatetime) FROM stdin;
fb747cq725lj	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
wsycyxw9kn5g	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
h479nl7yx9w2	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
ssn4bqkgn7gl	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
b55swlzgw778	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
4kyznty4fw3s	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
5p9y7rdc3t3q	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
wn9kbtypzth8	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
xmyvjwjvt5yc	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
yr9473tyn7qk	f	2018-03-08 15:31:03.38595+00	Changeset 9.30.1	\N	\N	\N
\.


SET search_path = notifygatewaysvc, pg_catalog;

--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

COPY databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
10.44.0-1	Philippe Brossier	database/changes/release-10.44.0/changelog.yml	2018-03-08 15:31:05.899189	1	EXECUTED	7:9e448dfafc920afa921269563a9038cb	sqlFile		\N	3.5.3	\N	\N	0523065747
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

COPY databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: message; Type: TABLE DATA; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

COPY message (messagepk, id, notificationid, optlockversion) FROM stdin;
\.


--
-- Name: messageseq; Type: SEQUENCE SET; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

SELECT pg_catalog.setval('messageseq', 1, false);


SET search_path = partysvc, pg_catalog;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: partysvc; Owner: postgres
--

COPY alembic_version (version_num) FROM stdin;
2798b5d5566a
\.


--
-- Data for Name: business; Type: TABLE DATA; Schema: partysvc; Owner: postgres
--

COPY business (party_uuid, business_ref, created_on) FROM stdin;
\.


--
-- Data for Name: business_attributes; Type: TABLE DATA; Schema: partysvc; Owner: postgres
--

COPY business_attributes (id, business_id, sample_summary_id, collection_exercise, attributes, created_on) FROM stdin;
\.


--
-- Name: business_attributes_id_seq; Type: SEQUENCE SET; Schema: partysvc; Owner: postgres
--

SELECT pg_catalog.setval('business_attributes_id_seq', 1, false);


--
-- Data for Name: business_respondent; Type: TABLE DATA; Schema: partysvc; Owner: postgres
--

COPY business_respondent (business_id, respondent_id, status, effective_from, effective_to, created_on) FROM stdin;
\.


--
-- Data for Name: enrolment; Type: TABLE DATA; Schema: partysvc; Owner: postgres
--

COPY enrolment (business_id, respondent_id, survey_id, survey_name, status, created_on) FROM stdin;
\.


--
-- Data for Name: pending_enrolment; Type: TABLE DATA; Schema: partysvc; Owner: postgres
--

COPY pending_enrolment (id, case_id, respondent_id, business_id, survey_id, created_on) FROM stdin;
\.


--
-- Name: pending_enrolment_id_seq; Type: SEQUENCE SET; Schema: partysvc; Owner: postgres
--

SELECT pg_catalog.setval('pending_enrolment_id_seq', 1, false);


--
-- Data for Name: respondent; Type: TABLE DATA; Schema: partysvc; Owner: postgres
--

COPY respondent (id, party_uuid, status, email_address, first_name, last_name, telephone, created_on) FROM stdin;
\.


--
-- Name: respondent_id_seq; Type: SEQUENCE SET; Schema: partysvc; Owner: postgres
--

SELECT pg_catalog.setval('respondent_id_seq', 1, false);


SET search_path = public, pg_catalog;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add o auth user	7	add_oauthuser
20	Can change o auth user	7	change_oauthuser
21	Can delete o auth user	7	delete_oauthuser
22	Can add o auth client	8	add_oauthclient
23	Can change o auth client	8	change_oauthclient
24	Can delete o auth client	8	delete_oauthclient
25	Can add o auth scope	9	add_oauthscope
26	Can change o auth scope	9	change_oauthscope
27	Can delete o auth scope	9	delete_oauthscope
28	Can add o auth refresh token	10	add_oauthrefreshtoken
29	Can change o auth refresh token	10	change_oauthrefreshtoken
30	Can delete o auth refresh token	10	delete_oauthrefreshtoken
31	Can add o auth access token	11	add_oauthaccesstoken
32	Can change o auth access token	11	change_oauthaccesstoken
33	Can delete o auth access token	11	delete_oauthaccesstoken
34	Can add o auth authorization code	12	add_oauthauthorizationcode
35	Can change o auth authorization code	12	change_oauthauthorizationcode
36	Can delete o auth authorization code	12	delete_oauthauthorizationcode
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 36, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$24000$0QjtBFfodgIm$5IlywhSFi5ysDsXHbc7/6S1+27ICrixDxKzvA+E3iOk=	\N	t	admin			admin@email.com	t	t	2018-03-08 15:29:59.975222+00
1	pbkdf2_sha256$24000$vZSUMt7MFzyW$2Wv7VKggLJ/G7N+i+gkgvyIfEy4atRlay9FTNrOs6c0=	\N	f	ons@ons.gov			ons@ons.gov	f	t	2018-03-08 15:30:01.386771+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 2, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: authz_approvals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY authz_approvals (user_id, client_id, scope, expiresat, status, lastmodifiedat, identity_zone_id) FROM stdin;
\.


--
-- Data for Name: credentials_oauthclient; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY credentials_oauthclient (id, password, client_id, redirect_uri) FROM stdin;
1	$2a$12$An0d09N/ZFL3LR1khGNtYOFNlBQy7nlzaB9fi9R8rA4u1IkFvzImK	ons@ons.gov	https://www.ons.gov.uk/
\.


--
-- Name: credentials_oauthclient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('credentials_oauthclient_id_seq', 1, true);


--
-- Data for Name: credentials_oauthuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY credentials_oauthuser (id, password, email, failed_logins, account_is_locked, account_is_verified) FROM stdin;
1	$2a$12$xf7ghr2LDskaBBvBrvH1euK83/Qls2TAx49hQpHtfzhayHGHDOCke	testuser@email.com	0	f	t
\.


--
-- Name: credentials_oauthuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('credentials_oauthuser_id_seq', 1, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	credentials	oauthuser
8	credentials	oauthclient
9	tokens	oauthscope
10	tokens	oauthrefreshtoken
11	tokens	oauthaccesstoken
12	tokens	oauthauthorizationcode
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 12, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-03-08 15:29:36.75943+00
2	auth	0001_initial	2018-03-08 15:29:36.85617+00
3	admin	0001_initial	2018-03-08 15:29:36.886451+00
4	admin	0002_logentry_remove_auto_add	2018-03-08 15:29:36.90476+00
5	contenttypes	0002_remove_content_type_name	2018-03-08 15:29:36.948583+00
6	auth	0002_alter_permission_name_max_length	2018-03-08 15:29:36.966154+00
7	auth	0003_alter_user_email_max_length	2018-03-08 15:29:36.995542+00
8	auth	0004_alter_user_username_opts	2018-03-08 15:29:37.033902+00
9	auth	0005_alter_user_last_login_null	2018-03-08 15:29:37.048798+00
10	auth	0006_require_contenttypes_0002	2018-03-08 15:29:37.051884+00
11	auth	0007_alter_validators_add_error_messages	2018-03-08 15:29:37.066567+00
12	credentials	0001_initial	2018-03-08 15:29:37.100931+00
13	credentials	0002_auto_20170330_1354	2018-03-08 15:29:37.116826+00
14	credentials	0003_oauthuser_failed_logins	2018-03-08 15:29:37.149231+00
15	credentials	0004_oauthuser_account_is_locked	2018-03-08 15:29:37.167861+00
16	credentials	0005_auto_20170407_1111	2018-03-08 15:29:37.222469+00
17	sessions	0001_initial	2018-03-08 15:29:37.260493+00
18	tokens	0001_initial	2018-03-08 15:29:37.578425+00
19	tokens	0002_auto_20170407_1111	2018-03-08 15:29:37.632374+00
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 19, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: expiring_code_store; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY expiring_code_store (code, expiresat, data, intent, identity_zone_id) FROM stdin;
\.


--
-- Data for Name: external_group_mapping; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY external_group_mapping (group_id, external_group, added, origin, identity_zone_id) FROM stdin;
903a6d5e-736a-4b35-83cd-142770c4231f	cn=test_org,ou=people,o=springsource,o=org	2018-03-08 15:31:50.899	ldap	uaa
\.


--
-- Data for Name: group_membership; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY group_membership (group_id, member_id, member_type, authorities, added, origin, identity_zone_id) FROM stdin;
6194891b-74f0-4b2b-8be7-0d80ab7e100a	34047c3e-1f40-4c4d-87aa-cff35e4d8edc	USER	\N	2018-03-08 15:31:34.238	uaa	uaa
cda313f0-0230-4530-9207-00717ab6523c	34047c3e-1f40-4c4d-87aa-cff35e4d8edc	USER	\N	2018-03-08 15:31:34.339	uaa	uaa
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY groups (id, displayname, created, lastmodified, version, identity_zone_id, description) FROM stdin;
6194891b-74f0-4b2b-8be7-0d80ab7e100a	scim.me	2018-03-08 15:31:33.898	2018-03-08 15:31:33.898	0	uaa	\N
8d91f00d-4e9f-45b1-a3cd-ee1e38bd5108	approvals.me	2018-03-08 15:31:34.039	2018-03-08 15:31:34.039	0	uaa	\N
64bec4c9-1a99-421d-ae5b-342275eaaef5	profile	2018-03-08 15:31:34.059	2018-03-08 15:31:34.059	0	uaa	\N
fc190bcd-62ae-498f-b1fe-059e8a85cea9	roles	2018-03-08 15:31:34.093	2018-03-08 15:31:34.093	0	uaa	\N
eac974eb-2809-4c1a-960b-d3b0767303a0	user_attributes	2018-03-08 15:31:34.139	2018-03-08 15:31:34.139	0	uaa	\N
34456502-b92c-4330-8ad9-b4ac018156ce	cloud_controller.admin	2018-03-08 15:31:50.342	2018-03-08 15:31:50.342	0	uaa	\N
2fceeefd-1a3b-4bee-bf38-c4329b25963e	oauth.approvals	2018-03-08 15:31:50.372	2018-03-08 15:31:50.372	0	uaa	\N
b9f3e6b0-8915-4283-bd2b-c2626f758c65	idps.write	2018-03-08 15:31:50.278	2018-03-08 15:31:50.704	1	uaa	Create and update identity providers
1806c4d0-b36a-4375-a718-05e742b97950	scim.zones	2018-03-08 15:31:50.327	2018-03-08 15:31:50.71	1	uaa	Control a user's ability to manage a zone
24294bf3-de44-4278-878a-7fb72729714c	oauth.approval	2018-03-08 15:31:50.351	2018-03-08 15:31:50.723	1	uaa	Manage approved scopes
4e76c7a7-422c-4bd0-8592-d1f6d74ed5f5	cloud_controller.write	2018-03-08 15:31:50.357	2018-03-08 15:31:50.73	1	uaa	Push applications to your account and create and bind services
cc607cff-ce5d-4c7a-81a3-1394b4745477	cloud_controller_service_permissions.read	2018-03-08 15:31:50.368	2018-03-08 15:31:50.734	1	uaa	Verify user permission to manage service instances
f4619ec4-2ee9-412b-91e7-8a2fb0f94066	uaa.none	2018-03-08 15:31:50.395	2018-03-08 15:31:50.737	1	uaa	Forbid acting as a user
606115e2-ce5d-4158-b396-ba63e6be98d0	idps.read	2018-03-08 15:31:50.419	2018-03-08 15:31:50.74	1	uaa	Retrieve identity providers
63a9e7d7-10e7-4e55-8a5e-42131b8f0805	clients.read	2018-03-08 15:31:50.451	2018-03-08 15:31:50.744	1	uaa	Read information about OAuth clients
e44d6760-45a9-429d-8fe3-ad674a484389	zones.read	2018-03-08 15:31:50.47	2018-03-08 15:31:50.746	1	uaa	Read identity zones
cda313f0-0230-4530-9207-00717ab6523c	scim.userids	2018-03-08 15:31:34.27	2018-03-08 15:31:50.749	1	uaa	Read user IDs and retrieve users by ID
7a829230-46c4-4207-ae44-bfd59ae1d14a	clients.secret	2018-03-08 15:31:50.498	2018-03-08 15:31:50.751	1	uaa	Change the password of an OAuth client
5600792e-14e7-4051-b752-fad8472998c6	uaa.resource	2018-03-08 15:31:50.549	2018-03-08 15:31:50.753	1	uaa	Serve resources protected by the UAA
d2fbb797-e7fc-4a73-8860-23bf39ae0f51	openid	2018-03-08 15:31:33.928	2018-03-08 15:31:50.755	1	uaa	Access profile information, i.e. email, first and last name, and phone number
89ec6f7e-5291-4fdb-b2eb-528c4733a1bf	scim.invite	2018-03-08 15:31:50.558	2018-03-08 15:31:50.757	1	uaa	Send invitations to users
e640a68f-b495-4a9c-a81f-2ba14e33704e	groups.update	2018-03-08 15:31:50.587	2018-03-08 15:31:50.759	1	uaa	Update group information and memberships
5e17389e-58cc-4263-9494-b85e381aaddb	oauth.login	2018-03-08 15:31:50.606	2018-03-08 15:31:50.763	1	uaa	Authenticate users outside of the UAA
83eecb1d-a373-4f53-a437-ef3604d7810c	uaa.admin	2018-03-08 15:31:50.623	2018-03-08 15:31:50.767	1	uaa	Act as an administrator throughout the UAA
885f8589-aa77-499d-bc6f-08958247b01a	clients.admin	2018-03-08 15:31:50.638	2018-03-08 15:31:50.771	1	uaa	Create, modify and delete OAuth clients
cd9f7c9a-cefe-4306-9859-fbfa378f1f8e	scim.read	2018-03-08 15:31:50.642	2018-03-08 15:31:50.773	1	uaa	Read all SCIM entities, i.e. users and groups
beee9b35-238d-4809-9ca7-7b35a1631fc4	scim.create	2018-03-08 15:31:50.655	2018-03-08 15:31:50.775	1	uaa	Create users
51f7c520-22a1-4e3f-a68b-290db043ed19	uaa.user	2018-03-08 15:31:33.979	2018-03-08 15:31:50.777	1	uaa	Act as a user in the UAA
f9deb5c0-88a9-4856-8949-dd89930b1ac8	cloud_controller.read	2018-03-08 15:31:50.663	2018-03-08 15:31:50.78	1	uaa	View details of your applications and services
ac31a48c-ebbe-4eb4-b827-3f444caff0a1	password.write	2018-03-08 15:31:33.959	2018-03-08 15:31:50.782	1	uaa	Change your password
73889ace-2ca1-47a8-b4d3-c9ec1237ee06	uaa.offline_token	2018-03-08 15:31:34.176	2018-03-08 15:31:50.785	1	uaa	Allow offline access
3aa06fa9-c7f2-432f-bd9c-7ffccf6c5a67	zones.write	2018-03-08 15:31:50.683	2018-03-08 15:31:50.787	1	uaa	Create and update identity zones
8199102f-8683-4220-82a4-914af6428986	clients.write	2018-03-08 15:31:50.69	2018-03-08 15:31:50.79	1	uaa	Create and modify OAuth clients
0ce73d97-feb4-4bcf-9c7e-48a735e757cb	scim.write	2018-03-08 15:31:50.699	2018-03-08 15:31:50.792	1	uaa	Create, modify and delete SCIM entities, i.e. users and groups
903a6d5e-736a-4b35-83cd-142770c4231f	organizations.acme	2018-03-08 15:31:50.88	2018-03-08 15:31:50.88	0	uaa	\N
\.


--
-- Data for Name: identity_provider; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY identity_provider (id, created, lastmodified, version, identity_zone_id, name, origin_key, type, config, active) FROM stdin;
b2d12e21-1cff-44b0-9772-ac43fe1d1dc6	2000-01-01 00:00:00	2000-01-01 00:00:00	0	uaa	login-server	login-server	login-server	\N	t
ccf4a9a6-10e7-4802-9885-ea6b23cd370d	2000-01-01 00:00:00	2000-01-01 00:00:00	0	uaa	keystone	keystone	keystone	\N	t
c9a96e6e-f512-4bed-8c58-1a59258af803	2000-01-01 00:00:00	2018-03-08 15:31:31.746	1	uaa	UAA LDAP Provider	ldap	ldap	{"emailDomain":null,"additionalConfiguration":null,"providerDescription":null,"externalGroupsWhitelist":[],"attributeMappings":{},"addShadowUserOnLogin":true,"storeCustomAttributes":true,"ldapProfileFile":null,"baseUrl":null,"referral":null,"skipSSLVerification":false,"userDNPattern":null,"userDNPatternDelimiter":null,"bindUserDn":null,"userSearchBase":null,"userSearchFilter":null,"passwordAttributeName":null,"passwordEncoder":null,"localPasswordCompare":null,"mailAttributeName":"mail","mailSubstitute":null,"mailSubstituteOverridesLdap":false,"ldapGroupFile":null,"groupSearchBase":null,"groupSearchFilter":null,"groupsIgnorePartialResults":null,"autoAddGroups":true,"groupSearchSubTree":true,"maxGroupSearchDepth":10,"groupRoleAttribute":null,"tlsConfiguration":"none"}	f
d3785876-3329-4f24-9dcb-1029ac398a95	2000-01-01 00:00:00	2018-03-08 15:31:34.45	1	uaa	uaa	uaa	uaa	{"emailDomain":null,"additionalConfiguration":null,"providerDescription":null,"passwordPolicy":{"minLength":0,"maxLength":255,"requireUpperCaseCharacter":0,"requireLowerCaseCharacter":0,"requireDigit":0,"requireSpecialCharacter":0,"passwordNewerThan":null,"expirePasswordInMonths":0},"lockoutPolicy":{"lockoutPeriodSeconds":300,"lockoutAfterFailures":5,"countFailuresWithin":1200},"disableInternalUserManagement":false}	t
\.


--
-- Data for Name: identity_zone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY identity_zone (id, created, lastmodified, version, subdomain, name, description, config) FROM stdin;
uaa	2000-01-01 00:00:00	2018-03-08 15:31:35.849	1		uaa	The system zone for backwards compatibility	{"clientSecretPolicy":{"minLength":0,"maxLength":255,"requireUpperCaseCharacter":0,"requireLowerCaseCharacter":0,"requireDigit":0,"requireSpecialCharacter":0},"tokenPolicy":{"accessTokenValidity":43200,"refreshTokenValidity":2592000,"jwtRevocable":false,"refreshTokenUnique":false,"refreshTokenFormat":"jwt","activeKeyId":null},"samlConfig":{"assertionSigned":true,"requestSigned":true,"wantAssertionSigned":true,"wantAuthnRequestSigned":false,"assertionTimeToLiveSeconds":600,"activeKeyId":"legacy-saml-key","keys":{"legacy-saml-key":{"key":"-----BEGIN RSA PRIVATE KEY-----\\nMIICXQIBAAKBgQDHtC5gUXxBKpEqZTLkNvFwNGnNIkggNOwOQVNbpO0WVHIivig5\\nL39WqS9u0hnA+O7MCA/KlrAR4bXaeVVhwfUPYBKIpaaTWFQR5cTR1UFZJL/OF9vA\\nfpOwznoD66DDCnQVpbCjtDYWX+x6imxn8HCYxhMol6ZnTbSsFW6VZjFMjQIDAQAB\\nAoGAVOj2Yvuigi6wJD99AO2fgF64sYCm/BKkX3dFEw0vxTPIh58kiRP554Xt5ges\\n7ZCqL9QpqrChUikO4kJ+nB8Uq2AvaZHbpCEUmbip06IlgdA440o0r0CPo1mgNxGu\\nlhiWRN43Lruzfh9qKPhleg2dvyFGQxy5Gk6KW/t8IS4x4r0CQQD/dceBA+Ndj3Xp\\nubHfxqNz4GTOxndc/AXAowPGpge2zpgIc7f50t8OHhG6XhsfJ0wyQEEvodDhZPYX\\nkKBnXNHzAkEAyCA76vAwuxqAd3MObhiebniAU3SnPf2u4fdL1EOm92dyFs1JxyyL\\ngu/DsjPjx6tRtn4YAalxCzmAMXFSb1qHfwJBAM3qx3z0gGKbUEWtPHcP7BNsrnWK\\nvw6By7VC8bk/ffpaP2yYspS66Le9fzbFwoDzMVVUO/dELVZyBnhqSRHoXQcCQQCe\\nA2WL8S5o7Vn19rC0GVgu3ZJlUrwiZEVLQdlrticFPXaFrn3Md82ICww3jmURaKHS\\nN+l4lnMda79eSp3OMmq9AkA0p79BvYsLshUJJnvbk76pCjR28PK4dV1gSDUEqQMB\\nqy45ptdwJLqLJCeNoR0JUcDNIRhOCuOPND7pcMtX6hI/\\n-----END RSA PRIVATE KEY-----\\n","passphrase":"password","certificate":"-----BEGIN CERTIFICATE-----\\nMIIDSTCCArKgAwIBAgIBADANBgkqhkiG9w0BAQQFADB8MQswCQYDVQQGEwJhdzEO\\nMAwGA1UECBMFYXJ1YmExDjAMBgNVBAoTBWFydWJhMQ4wDAYDVQQHEwVhcnViYTEO\\nMAwGA1UECxMFYXJ1YmExDjAMBgNVBAMTBWFydWJhMR0wGwYJKoZIhvcNAQkBFg5h\\ncnViYUBhcnViYS5hcjAeFw0xNTExMjAyMjI2MjdaFw0xNjExMTkyMjI2MjdaMHwx\\nCzAJBgNVBAYTAmF3MQ4wDAYDVQQIEwVhcnViYTEOMAwGA1UEChMFYXJ1YmExDjAM\\nBgNVBAcTBWFydWJhMQ4wDAYDVQQLEwVhcnViYTEOMAwGA1UEAxMFYXJ1YmExHTAb\\nBgkqhkiG9w0BCQEWDmFydWJhQGFydWJhLmFyMIGfMA0GCSqGSIb3DQEBAQUAA4GN\\nADCBiQKBgQDHtC5gUXxBKpEqZTLkNvFwNGnNIkggNOwOQVNbpO0WVHIivig5L39W\\nqS9u0hnA+O7MCA/KlrAR4bXaeVVhwfUPYBKIpaaTWFQR5cTR1UFZJL/OF9vAfpOw\\nznoD66DDCnQVpbCjtDYWX+x6imxn8HCYxhMol6ZnTbSsFW6VZjFMjQIDAQABo4Ha\\nMIHXMB0GA1UdDgQWBBTx0lDzjH/iOBnOSQaSEWQLx1syGDCBpwYDVR0jBIGfMIGc\\ngBTx0lDzjH/iOBnOSQaSEWQLx1syGKGBgKR+MHwxCzAJBgNVBAYTAmF3MQ4wDAYD\\nVQQIEwVhcnViYTEOMAwGA1UEChMFYXJ1YmExDjAMBgNVBAcTBWFydWJhMQ4wDAYD\\nVQQLEwVhcnViYTEOMAwGA1UEAxMFYXJ1YmExHTAbBgkqhkiG9w0BCQEWDmFydWJh\\nQGFydWJhLmFyggEAMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEEBQADgYEAYvBJ\\n0HOZbbHClXmGUjGs+GS+xC1FO/am2suCSYqNB9dyMXfOWiJ1+TLJk+o/YZt8vuxC\\nKdcZYgl4l/L6PxJ982SRhc83ZW2dkAZI4M0/Ud3oePe84k8jm3A7EvH5wi5hvCkK\\nRpuRBwn3Ei+jCRouxTbzKPsuCVB+1sNyxMTXzf0=\\n-----END CERTIFICATE-----\\n"}},"disableInResponseToCheck":false,"privateKey":"-----BEGIN RSA PRIVATE KEY-----\\nMIICXQIBAAKBgQDHtC5gUXxBKpEqZTLkNvFwNGnNIkggNOwOQVNbpO0WVHIivig5\\nL39WqS9u0hnA+O7MCA/KlrAR4bXaeVVhwfUPYBKIpaaTWFQR5cTR1UFZJL/OF9vA\\nfpOwznoD66DDCnQVpbCjtDYWX+x6imxn8HCYxhMol6ZnTbSsFW6VZjFMjQIDAQAB\\nAoGAVOj2Yvuigi6wJD99AO2fgF64sYCm/BKkX3dFEw0vxTPIh58kiRP554Xt5ges\\n7ZCqL9QpqrChUikO4kJ+nB8Uq2AvaZHbpCEUmbip06IlgdA440o0r0CPo1mgNxGu\\nlhiWRN43Lruzfh9qKPhleg2dvyFGQxy5Gk6KW/t8IS4x4r0CQQD/dceBA+Ndj3Xp\\nubHfxqNz4GTOxndc/AXAowPGpge2zpgIc7f50t8OHhG6XhsfJ0wyQEEvodDhZPYX\\nkKBnXNHzAkEAyCA76vAwuxqAd3MObhiebniAU3SnPf2u4fdL1EOm92dyFs1JxyyL\\ngu/DsjPjx6tRtn4YAalxCzmAMXFSb1qHfwJBAM3qx3z0gGKbUEWtPHcP7BNsrnWK\\nvw6By7VC8bk/ffpaP2yYspS66Le9fzbFwoDzMVVUO/dELVZyBnhqSRHoXQcCQQCe\\nA2WL8S5o7Vn19rC0GVgu3ZJlUrwiZEVLQdlrticFPXaFrn3Md82ICww3jmURaKHS\\nN+l4lnMda79eSp3OMmq9AkA0p79BvYsLshUJJnvbk76pCjR28PK4dV1gSDUEqQMB\\nqy45ptdwJLqLJCeNoR0JUcDNIRhOCuOPND7pcMtX6hI/\\n-----END RSA PRIVATE KEY-----\\n","privateKeyPassword":"password","certificate":"-----BEGIN CERTIFICATE-----\\nMIIDSTCCArKgAwIBAgIBADANBgkqhkiG9w0BAQQFADB8MQswCQYDVQQGEwJhdzEO\\nMAwGA1UECBMFYXJ1YmExDjAMBgNVBAoTBWFydWJhMQ4wDAYDVQQHEwVhcnViYTEO\\nMAwGA1UECxMFYXJ1YmExDjAMBgNVBAMTBWFydWJhMR0wGwYJKoZIhvcNAQkBFg5h\\ncnViYUBhcnViYS5hcjAeFw0xNTExMjAyMjI2MjdaFw0xNjExMTkyMjI2MjdaMHwx\\nCzAJBgNVBAYTAmF3MQ4wDAYDVQQIEwVhcnViYTEOMAwGA1UEChMFYXJ1YmExDjAM\\nBgNVBAcTBWFydWJhMQ4wDAYDVQQLEwVhcnViYTEOMAwGA1UEAxMFYXJ1YmExHTAb\\nBgkqhkiG9w0BCQEWDmFydWJhQGFydWJhLmFyMIGfMA0GCSqGSIb3DQEBAQUAA4GN\\nADCBiQKBgQDHtC5gUXxBKpEqZTLkNvFwNGnNIkggNOwOQVNbpO0WVHIivig5L39W\\nqS9u0hnA+O7MCA/KlrAR4bXaeVVhwfUPYBKIpaaTWFQR5cTR1UFZJL/OF9vAfpOw\\nznoD66DDCnQVpbCjtDYWX+x6imxn8HCYxhMol6ZnTbSsFW6VZjFMjQIDAQABo4Ha\\nMIHXMB0GA1UdDgQWBBTx0lDzjH/iOBnOSQaSEWQLx1syGDCBpwYDVR0jBIGfMIGc\\ngBTx0lDzjH/iOBnOSQaSEWQLx1syGKGBgKR+MHwxCzAJBgNVBAYTAmF3MQ4wDAYD\\nVQQIEwVhcnViYTEOMAwGA1UEChMFYXJ1YmExDjAMBgNVBAcTBWFydWJhMQ4wDAYD\\nVQQLEwVhcnViYTEOMAwGA1UEAxMFYXJ1YmExHTAbBgkqhkiG9w0BCQEWDmFydWJh\\nQGFydWJhLmFyggEAMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEEBQADgYEAYvBJ\\n0HOZbbHClXmGUjGs+GS+xC1FO/am2suCSYqNB9dyMXfOWiJ1+TLJk+o/YZt8vuxC\\nKdcZYgl4l/L6PxJ982SRhc83ZW2dkAZI4M0/Ud3oePe84k8jm3A7EvH5wi5hvCkK\\nRpuRBwn3Ei+jCRouxTbzKPsuCVB+1sNyxMTXzf0=\\n-----END CERTIFICATE-----\\n"},"corsPolicy":{"xhrConfiguration":{"allowedOrigins":[".*"],"allowedOriginPatterns":[],"allowedUris":[".*"],"allowedUriPatterns":[],"allowedHeaders":["Accept","Authorization","Content-Type"],"allowedMethods":["GET"],"allowedCredentials":false,"maxAge":1728000},"defaultConfiguration":{"allowedOrigins":[".*"],"allowedOriginPatterns":[],"allowedUris":[".*"],"allowedUriPatterns":[],"allowedHeaders":["Accept","Authorization","Content-Type"],"allowedMethods":["GET"],"allowedCredentials":false,"maxAge":1728000}},"links":{"logout":{"redirectUrl":"/login","redirectParameterName":"redirect","disableRedirectParameter":false,"whitelist":null},"selfService":{"selfServiceLinksEnabled":true,"signup":null,"passwd":null}},"prompts":[{"name":"username","type":"text","text":"Email"},{"name":"password","type":"password","text":"Password"},{"name":"passcode","type":"password","text":"One Time Code ( Get one at http://localhost:8080/uaa/passcode )"}],"idpDiscoveryEnabled":false,"accountChooserEnabled":false,"userConfig":{"defaultGroups":["openid","scim.me","cloud_controller.read","cloud_controller.write","cloud_controller_service_permissions.read","password.write","scim.userids","uaa.user","approvals.me","oauth.approvals","profile","roles","user_attributes","uaa.offline_token"]},"mfaConfig":{"enabled":false}}
\.


--
-- Data for Name: mfa_providers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY mfa_providers (id, created, lastmodified, identity_zone_id, name, type, config) FROM stdin;
\.


--
-- Data for Name: oauth_client_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY oauth_client_details (client_id, resource_ids, client_secret, scope, authorized_grant_types, web_server_redirect_uri, authorities, access_token_validity, refresh_token_validity, additional_information, autoapprove, identity_zone_id, lastmodified, show_on_home_page, app_launch_url, app_icon, created_by, required_user_groups) FROM stdin;
ras_backstage	none	$2a$10$rEg.JLOBdFTGs9svBuPa.u9FjU.JsIXeaUoeCSL6JfBG0sNPCVD3a	scim.userids, scim.me, scim.read	client_credentials,password	\N	scim.userids,scim.me,scim.read	\N	\N	{}		uaa	2018-03-08 15:31:47.142	f	\N	\\x	\N	\N
admin	none	$2a$10$89itchCMOI.EW8e8WVk/mukzUurvxoEYMthuOZvNwIbsgRYwbqT1m	uaa.admin	client_credentials	\N	uaa.admin,clients.all,scim.all	\N	\N	{}		uaa	2018-03-08 15:31:47.565	f	\N	\\x	\N	\N
login	none	$2a$10$aqhN6QPEkPySOWji0qLoae6Jssc1phzUQHukHlPp9/I0HKySkOkye	uaa.none	client_credentials	\N	scim.all,clients.all	\N	\N	{}		uaa	2018-03-08 15:31:47.76	f	\N	\\x	\N	\N
secure_message	none	$2a$10$d0k9fNSM1SiY0nECj2vENe0KSqPqm2wKuwN21GGzqiK5PWSIf9cx.	scim.userids, scim.me, scim.read	client_credentials	\N	scim.userids,scim.me,scim.read	\N	\N	{}		uaa	2018-03-08 15:31:47.9	f	\N	\\x	\N	\N
\.


--
-- Data for Name: oauth_code; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY oauth_code (code, authentication, created, expiresat, user_id, client_id, identity_zone_id) FROM stdin;
\.


--
-- Data for Name: revocable_tokens; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY revocable_tokens (token_id, client_id, user_id, format, response_type, issued_at, expires_at, scope, data, identity_zone_id) FROM stdin;
7e7d19cc30d44c55b8316cdeaa65ae60	secure_message	\N	OPAQUE	ACCESS_TOKEN	1520523124930	1520566324772	[scim.userids, scim.me, scim.read]	eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI3ZTdkMTljYzMwZDQ0YzU1YjgzMTZjZGVhYTY1YWU2MCIsInN1YiI6InNlY3VyZV9tZXNzYWdlIiwiYXV0aG9yaXRpZXMiOlsic2NpbS5tZSIsInNjaW0udXNlcmlkcyIsInNjaW0ucmVhZCJdLCJzY29wZSI6WyJzY2ltLnVzZXJpZHMiLCJzY2ltLm1lIiwic2NpbS5yZWFkIl0sImNsaWVudF9pZCI6InNlY3VyZV9tZXNzYWdlIiwiY2lkIjoic2VjdXJlX21lc3NhZ2UiLCJhenAiOiJzZWN1cmVfbWVzc2FnZSIsInJldm9jYWJsZSI6dHJ1ZSwiZ3JhbnRfdHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsInJldl9zaWciOiJjZmMxYjE1ZCIsImlhdCI6MTUyMDUyMzEyNCwiZXhwIjoxNTIwNTY2MzI0LCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvdWFhL29hdXRoL3Rva2VuIiwiemlkIjoidWFhIiwiYXVkIjpbInNjaW0iLCJzZWN1cmVfbWVzc2FnZSJdfQ.HGshPQQMF3M6TvmnOGsf7nws-vgb0rgwJLMEp-xACGvmY6YjLmUki6_nwEgesuxoJCsMA9dxIJZbV_W80rJmXdIYdmSgarefg9ZddN_iWGg8wDomMRIXEe59q9pxti4Szra9r8jLQ_Cmff4iIaopPIJu3PSwWpBas333zl89XR-9yQTMozIbW0r1gn6suCncWpXRFiDP0jJQ5iNC8vj1qDkgWhN-1a29UEljv2rlQ6Vnx-pCCZHeZ3hze4MTRysqqUf96w2-O9SRI63ySpZv1Pm5pHDiDcipET_nR5c6V-Mxyu61V2j12iz1TLb4hmryDbm0WWi1ulFF0XCGwRbH8g	uaa
fa12614a34d64bd6bd88a544e2f80d98	secure_message	\N	OPAQUE	ACCESS_TOKEN	1520523127588	1520566327518	[scim.userids, scim.me, scim.read]	eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiJmYTEyNjE0YTM0ZDY0YmQ2YmQ4OGE1NDRlMmY4MGQ5OCIsInN1YiI6InNlY3VyZV9tZXNzYWdlIiwiYXV0aG9yaXRpZXMiOlsic2NpbS5tZSIsInNjaW0udXNlcmlkcyIsInNjaW0ucmVhZCJdLCJzY29wZSI6WyJzY2ltLnVzZXJpZHMiLCJzY2ltLm1lIiwic2NpbS5yZWFkIl0sImNsaWVudF9pZCI6InNlY3VyZV9tZXNzYWdlIiwiY2lkIjoic2VjdXJlX21lc3NhZ2UiLCJhenAiOiJzZWN1cmVfbWVzc2FnZSIsInJldm9jYWJsZSI6dHJ1ZSwiZ3JhbnRfdHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsInJldl9zaWciOiJjZmMxYjE1ZCIsImlhdCI6MTUyMDUyMzEyNywiZXhwIjoxNTIwNTY2MzI3LCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvdWFhL29hdXRoL3Rva2VuIiwiemlkIjoidWFhIiwiYXVkIjpbInNjaW0iLCJzZWN1cmVfbWVzc2FnZSJdfQ.nHkFvhefw4Zyt1XWkXVjL-3n_TLa4M94KP_mqGMcauer8f79OgBESVk-MxCG_M88ltfq72XrmmP46VmY26vmuXh5I1mN52wS-3svq6x6iaRDZWxftj2ouz44DVHHQQHvqeVxwlt5-rJiMIbnzEpYOFD6XDgjqnnmXOLLJkzUHIT6JWTLCbB4cZO7vNLnkd6IVVFkmzasJk6QxOrjZzKgg6mA9To2p53Ph5WWnrPWe78Gax9tA-0pMMrls5QCXHBVFf1XXufliLDYWGrYueJ6JzP1BNfKqyWHrj8Kb5IyXM_Tl6AQ9gpsdCR5J1g3z-uchLhyTMSp0KViOhEwfGa3Gg	uaa
\.


--
-- Data for Name: schema_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY schema_version (installed_rank, version, description, type, script, checksum, installed_by, installed_on, execution_time, success) FROM stdin;
1	1.5.2	<< Flyway Baseline >>	BASELINE	<< Flyway Baseline >>	\N	postgres	2018-03-08 15:31:05.607826	0	t
2	1.5.3	InitialDBScript	JDBC	org.cloudfoundry.identity.uaa.db.postgresql.V1_5_3__InitialDBScript	\N	postgres	2018-03-08 15:31:06.599029	234	t
3	1.5.4	NormalizeTableAndColumnNames	SPRING_JDBC	org.cloudfoundry.identity.uaa.db.postgresql.V1_5_4__NormalizeTableAndColumnNames	\N	postgres	2018-03-08 15:31:06.859148	146	t
4	1.5.5	CreateExpiringCodeStore	SQL	V1_5_5__CreateExpiringCodeStore.sql	-2020719372	postgres	2018-03-08 15:31:07.054577	21	t
5	1.6.0	ExtendAuthzApprovalUsername	SQL	V1_6_0__ExtendAuthzApprovalUsername.sql	-1817446962	postgres	2018-03-08 15:31:07.107412	25	t
6	1.7.0	OriginAndExternalIDColumns	SQL	V1_7_0__OriginAndExternalIDColumns.sql	-1606261320	postgres	2018-03-08 15:31:07.151541	39	t
7	1.7.1	OriginForGroupMembershipColumns	SQL	V1_7_1__OriginForGroupMembershipColumns.sql	2015853392	postgres	2018-03-08 15:31:07.253718	10	t
8	1.7.3	ExtendClientAuthorities	SQL	V1_7_3__ExtendClientAuthorities.sql	-1195677722	postgres	2018-03-08 15:31:07.332494	17	t
9	1.8.2	DropCorrectPostgreSQLIndex	SQL	V1_8_2__DropCorrectPostgreSQLIndex.sql	1875410207	postgres	2018-03-08 15:31:07.373031	16	t
10	1.8.4	Add AutoApproveField	SQL	V1_8_4__Add_AutoApproveField.sql	-62269219	postgres	2018-03-08 15:31:07.428943	32	t
11	1.10.0	SetVerifiedToTrueForExistingUsers	SQL	V1_10_0__SetVerifiedToTrueForExistingUsers.sql	-1856645855	postgres	2018-03-08 15:31:07.520174	3	t
12	2.0.0	Multitenancy	SQL	V2_0_0__Multitenancy.sql	-438860248	postgres	2018-03-08 15:31:07.547304	130	t
13	2.0.2	BootstrapIdentityZones	SPRING_JDBC	org.cloudfoundry.identity.uaa.db.postgresql.V2_0_2__BootstrapIdentityZones	\N	postgres	2018-03-08 15:31:07.69259	63	t
14	2.0.3	PostBootstrapIdentityZones	SQL	V2_0_3__PostBootstrapIdentityZones.sql	-692328688	postgres	2018-03-08 15:31:07.779586	11	t
15	2.0.4	Identity Provider Adjustments	SQL	V2_0_4__Identity_Provider_Adjustments.sql	726038816	postgres	2018-03-08 15:31:07.807955	42	t
16	2.0.5	Default uaa	SQL	V2_0_5__Default_uaa.sql	-125973374	postgres	2018-03-08 15:31:07.88821	21	t
17	2.0.6	Audit identity zone	SQL	V2_0_6__Audit_identity_zone.sql	1262295991	postgres	2018-03-08 15:31:07.92851	44	t
18	2.1.0	Identity Provider Update UAA Type	SQL	V2_1_0__Identity_Provider_Update_UAA_Type.sql	1835283239	postgres	2018-03-08 15:31:07.970827	19	t
19	2.1.1	Add Last Modified To Client Details	SQL	V2_1_1__Add_Last_Modified_To_Client_Details.sql	1067837267	postgres	2018-03-08 15:31:08.027958	43	t
20	2.3.0	Add SaltFieldsToUsers	SQL	V2_3_0__Add_SaltFieldsToUsers.sql	1026275124	postgres	2018-03-08 15:31:08.120192	23	t
21	2.3.1	Add Index To Users Email	SQL	V2_3_1__Add_Index_To_Users_Email.sql	657518892	postgres	2018-03-08 15:31:08.167999	10	t
22	2.3.2	Add Password Last Modified To Users	SQL	V2_3_2__Add_Password_Last_Modified_To_Users.sql	-1175051659	postgres	2018-03-08 15:31:08.192093	2	t
23	2.3.3	ExtendApprovalClientId	SQL	V2_3_3__ExtendApprovalClientId.sql	127936416	postgres	2018-03-08 15:31:08.208993	45	t
24	2.3.4	SetDefaultUaaPasswordPolicy	SQL	V2_3_4__SetDefaultUaaPasswordPolicy.sql	1827450134	postgres	2018-03-08 15:31:08.279774	2	t
25	2.3.5	LenientDefaultUaaPasswordPolicy	SQL	V2_3_5__LenientDefaultUaaPasswordPolicy.sql	1331153366	postgres	2018-03-08 15:31:08.291379	18	t
26	2.3.6	Add Index To Users Id	SQL	V2_3_6__Add_Index_To_Users_Id.sql	-1480638944	postgres	2018-03-08 15:31:08.360129	27	t
27	2.4.0	OauthCodeTableImprovements	SQL	V2_4_0__OauthCodeTableImprovements.sql	1114503935	postgres	2018-03-08 15:31:08.445024	25	t
28	2.4.1	Zonify Group Memberships	SQL	V2_4_1__Zonify_Group_Memberships.sql	-1407992365	postgres	2018-03-08 15:31:08.530389	17	t
29	2.5.0	Fix Verified Column	SQL	V2_5_0__Fix_Verified_Column.sql	1522218930	postgres	2018-03-08 15:31:08.583082	16	t
30	2.5.1	Fix Null Values In GroupMbr ZoneId	SQL	V2_5_1__Fix_Null_Values_In_GroupMbr_ZoneId.sql	1958229631	postgres	2018-03-08 15:31:08.621167	25	t
31	2.5.2	Zonify Groups	SQL	V2_5_2__Zonify_Groups.sql	-1357063013	postgres	2018-03-08 15:31:08.681259	46	t
32	2.5.3	Migrate Groups For Zones	SPRING_JDBC	org.cloudfoundry.identity.uaa.db.postgresql.V2_5_3__Migrate_Groups_For_Zones	\N	postgres	2018-03-08 15:31:08.810673	17	t
33	2.5.4	Zonify Groups	SQL	V2_5_4__Zonify_Groups.sql	-234989374	postgres	2018-03-08 15:31:08.876229	24	t
34	2.7.0	Allow User Management	SQL	V2_7_0__Allow_User_Management.sql	-876867242	postgres	2018-03-08 15:31:08.911719	37	t
35	2.7.0.1	Fix Client Id Length	SQL	V2_7_0_1__Fix_Client_Id_Length.sql	1695494357	postgres	2018-03-08 15:31:08.977599	15	t
36	2.7.1	Update User Management	SQL	V2_7_1__Update_User_Management.sql	-272854847	postgres	2018-03-08 15:31:09.018385	28	t
37	2.7.2	Drop User Management	SQL	V2_7_2__Drop_User_Management.sql	-108533325	postgres	2018-03-08 15:31:09.056755	2	t
38	2.7.3	Migrate Zone Subdomain To Lowercase	SPRING_JDBC	org.cloudfoundry.identity.uaa.db.postgresql.V2_7_3__Migrate_Zone_Subdomain_To_Lowercase	\N	postgres	2018-03-08 15:31:09.086615	4	t
39	2.7.4	Add Config To Identity Zone	SQL	V2_7_4__Add_Config_To_Identity_Zone.sql	-320296009	postgres	2018-03-08 15:31:09.108761	6	t
40	2.7.5	Add Intent to Expiring Code Store	SQL	V2_7_5__Add_Intent_to_Expiring_Code_Store.sql	244696293	postgres	2018-03-08 15:31:09.126131	2	t
41	3.0.0	Old Users For Verification Bleedover	SQL	V3_0_0__Old_Users_For_Verification_Bleedover.sql	-992556611	postgres	2018-03-08 15:31:09.144386	40	t
42	3.0.1	Add Group Description	SQL	V3_0_1__Add_Group_Description.sql	1870074679	postgres	2018-03-08 15:31:09.197954	10	t
43	3.0.2	Add Client Metadata Columns	SQL	V3_0_2__Add_Client_Metadata_Columns.sql	-696275591	postgres	2018-03-08 15:31:09.217683	13	t
44	3.0.3	SAML SP Management	SQL	V3_0_3__SAML_SP_Management.sql	1698810304	postgres	2018-03-08 15:31:09.242836	20	t
45	3.1.1	RevocableToken	SQL	V3_1_1__RevocableToken.sql	-310533425	postgres	2018-03-08 15:31:09.272391	28	t
46	3.3.0	RevocableToken Add ZoneId	SQL	V3_3_0__RevocableToken_Add_ZoneId.sql	-883678006	postgres	2018-03-08 15:31:09.341485	36	t
47	3.5.0	Drop Client IDP Table	SQL	V3_5_0__Drop_Client_IDP_Table.sql	727510794	postgres	2018-03-08 15:31:09.397431	33	t
48	3.5.1	Drop Authority From Users	SQL	V3_5_1__Drop_Authority_From_Users.sql	310838460	postgres	2018-03-08 15:31:09.490346	2	t
49	3.9.0	Add Index To GroupMembership Member Id	SQL	V3_9_0__Add_Index_To_GroupMembership_Member_Id.sql	61080735	postgres	2018-03-08 15:31:09.518256	25	t
50	3.9.1	PasswordChangeRequired	SQL	V3_9_1__PasswordChangeRequired.sql	1039242286	postgres	2018-03-08 15:31:09.540531	29	t
51	3.10.0	UserInfo	SQL	V3_10_0__UserInfo.sql	248204806	postgres	2018-03-08 15:31:09.581056	8	t
52	3.10.1	Add Last Logon To User	SQL	V3_10_1__Add_Last_Logon_To_User.sql	-1980479202	postgres	2018-03-08 15:31:09.599432	1	t
53	3.10.2	Add Created By To Oauth Client Details	SQL	V3_10_2__Add_Created_By_To_Oauth_Client_Details.sql	694593842	postgres	2018-03-08 15:31:09.609579	26	t
54	3.10.3	Add Previous Logon To User	SQL	V3_10_3__Add_Previous_Logon_To_User.sql	1216193350	postgres	2018-03-08 15:31:09.648411	2	t
55	4.0.1	Add Index To Sec Audit	SQL	V4_0_1__Add_Index_To_Sec_Audit.sql	-900061926	postgres	2018-03-08 15:31:09.668157	19	t
56	4.0.2	Add Required User Groups	SQL	V4_0_2__Add_Required_User_Groups.sql	-2114805334	postgres	2018-03-08 15:31:09.691004	1	t
57	4.0.3	Add Index To Oauth Code	SQL	V4_0_3__Add_Index_To_Oauth_Code.sql	835885118	postgres	2018-03-08 15:31:09.704549	7	t
58	4.0.4	FixFailedBackPortMigrations	JDBC	org.cloudfoundry.identity.uaa.db.postgresql.V4_0_4__FixFailedBackPortMigrations	\N	postgres	2018-03-08 15:31:09.720781	27	t
59	4.0.5	Add Identity Zone Id To Authz Approvals	SQL	V4_0_5__Add_Identity_Zone_Id_To_Authz_Approvals.sql	1334370415	postgres	2018-03-08 15:31:09.757735	6	t
60	4.0.6	Add Identity Zone Id To Tables	SQL	V4_0_6__Add_Identity_Zone_Id_To_Tables.sql	-483578542	postgres	2018-03-08 15:31:09.778444	16	t
61	4.0.7	Drop Old Authz Table	SQL	V4_0_7__Drop_Old_Authz_Table.sql	222527551	postgres	2018-03-08 15:31:09.799792	2	t
62	4.0.8	Add Index On Identity Zone To Revocable Tokens	SQL	V4_0_8__Add_Index_On_Identity_Zone_To_Revocable_Tokens.sql	1219563963	postgres	2018-03-08 15:31:09.82099	4	t
63	4.0.9	ExtendClientAuthScopeSize	SQL	V4_0_9__ExtendClientAuthScopeSize.sql	1307405486	postgres	2018-03-08 15:31:09.832066	2	t
64	4.0.10	ExpiringCode Add ZoneId	SQL	V4_0_10__ExpiringCode_Add_ZoneId.sql	1543841099	postgres	2018-03-08 15:31:09.843261	12	t
65	4.6.0	Add Perf Index To GroupMembership Group Id	SQL	V4_6_0__Add_Perf_Index_To_GroupMembership_Group_Id.sql	912666805	postgres	2018-03-08 15:31:09.866801	9	t
66	4.7.0	Remove Group Member Roles	SQL	V4_7_0__Remove_Group_Member_Roles.sql	2013062640	postgres	2018-03-08 15:31:09.888414	2	t
67	4.7.1	Add Mfa Providers Table	SQL	V4_7_1__Add_Mfa_Providers_Table.sql	89706304	postgres	2018-03-08 15:31:09.898034	9	t
68	4.7.2	Add Google Mfa User Creds Table	SQL	V4_7_2__Add_Google_Mfa_User_Creds_Table.sql	191022528	postgres	2018-03-08 15:31:09.915843	10	t
69	4.7.3	Remove Mfa Providers Active	SQL	V4_7_3__Remove_Mfa_Providers_Active.sql	-812895234	postgres	2018-03-08 15:31:09.933941	1	t
70	4.8.0	UniqueMfaName	SQL	V4_8_0__UniqueMfaName.sql	-394803959	postgres	2018-03-08 15:31:09.95755	4	t
71	4.8.1	AddMfaProviderToUserCredsTable	SQL	V4_8_1__AddMfaProviderToUserCredsTable.sql	396964362	postgres	2018-03-08 15:31:09.972117	1	t
72	4.8.2	AddZoneToUserCredsTable	SQL	V4_8_2__AddZoneToUserCredsTable.sql	-2091431375	postgres	2018-03-08 15:31:09.98112	1	t
73	4.8.3	SwapMfaUserCredPrimaryKey	SQL	V4_8_3__SwapMfaUserCredPrimaryKey.sql	2946552	postgres	2018-03-08 15:31:09.990174	5	t
74	4.9.0	Add Index To Groups Name	SQL	V4_9_0__Add_Index_To_Groups_Name.sql	-366559796	postgres	2018-03-08 15:31:10.021439	5	t
75	4.9.1	Extend client scopes authorities	SQL	V4_9_1__Extend_client_scopes_authorities.sql	2122621621	postgres	2018-03-08 15:31:10.03569	3	t
\.


--
-- Data for Name: sec_audit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY sec_audit (principal_id, event_type, origin, event_data, created, identity_zone_id) FROM stdin;
\.


--
-- Data for Name: service_provider; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY service_provider (id, created, lastmodified, version, identity_zone_id, name, entity_id, config, active) FROM stdin;
\.


--
-- Data for Name: tokens_oauthaccesstoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tokens_oauthaccesstoken (id, expires_at, access_token, client_id, refresh_token_id, user_id) FROM stdin;
\.


--
-- Name: tokens_oauthaccesstoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tokens_oauthaccesstoken_id_seq', 1, false);


--
-- Data for Name: tokens_oauthaccesstoken_scopes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tokens_oauthaccesstoken_scopes (id, oauthaccesstoken_id, oauthscope_id) FROM stdin;
\.


--
-- Name: tokens_oauthaccesstoken_scopes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tokens_oauthaccesstoken_scopes_id_seq', 1, false);


--
-- Data for Name: tokens_oauthauthorizationcode; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tokens_oauthauthorizationcode (id, expires_at, code, redirect_uri, client_id, user_id) FROM stdin;
\.


--
-- Name: tokens_oauthauthorizationcode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tokens_oauthauthorizationcode_id_seq', 1, false);


--
-- Data for Name: tokens_oauthauthorizationcode_scopes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tokens_oauthauthorizationcode_scopes (id, oauthauthorizationcode_id, oauthscope_id) FROM stdin;
\.


--
-- Name: tokens_oauthauthorizationcode_scopes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tokens_oauthauthorizationcode_scopes_id_seq', 1, false);


--
-- Data for Name: tokens_oauthrefreshtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tokens_oauthrefreshtoken (id, expires_at, refresh_token) FROM stdin;
\.


--
-- Name: tokens_oauthrefreshtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tokens_oauthrefreshtoken_id_seq', 1, false);


--
-- Data for Name: tokens_oauthscope; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tokens_oauthscope (id, scope, description, is_default) FROM stdin;
\.


--
-- Name: tokens_oauthscope_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tokens_oauthscope_id_seq', 1, false);


--
-- Data for Name: user_google_mfa_credentials; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY user_google_mfa_credentials (user_id, secret_key, validation_code, scratch_codes, mfa_provider_id, zone_id) FROM stdin;
\.


--
-- Data for Name: user_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY user_info (user_id, info) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users (id, created, lastmodified, version, username, password, email, givenname, familyname, active, phonenumber, authorities, verified, origin, external_id, identity_zone_id, salt, passwd_lastmodified, legacy_verification_behavior, passwd_change_required, last_logon_success_time, previous_logon_success_time) FROM stdin;
34047c3e-1f40-4c4d-87aa-cff35e4d8edc	2018-03-08 15:31:33.681	2018-03-08 15:31:33.681	0	uaa_user	$2a$10$0nVMCYY/IWRZw2oMtbBss.IQL2zO7jRpbbzlPTgnlNyWHrSbf5cGC	uaa_user	\N	\N	t	\N	uaa.user	t	uaa	\N	uaa	\N	2018-03-08 15:31:33	f	f	\N	\N
\.


SET search_path = ras_ci, pg_catalog;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY alembic_version (version_num) FROM stdin;
ccd22863e633
\.


--
-- Data for Name: business; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY business (id, ru_ref) FROM stdin;
\.


--
-- Name: business_id_seq; Type: SEQUENCE SET; Schema: ras_ci; Owner: postgres
--

SELECT pg_catalog.setval('business_id_seq', 1, false);


--
-- Data for Name: exercise; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY exercise (id, exercise_id, items, status) FROM stdin;
\.


--
-- Name: exercise_id_seq; Type: SEQUENCE SET; Schema: ras_ci; Owner: postgres
--

SELECT pg_catalog.setval('exercise_id_seq', 1, false);


--
-- Data for Name: instrument; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY instrument (id, type, instrument_id, stamp, survey_id, classifiers) FROM stdin;
\.


--
-- Data for Name: instrument_business; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY instrument_business (instrument_id, business_id) FROM stdin;
\.


--
-- Data for Name: instrument_exercise; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY instrument_exercise (instrument_id, exercise_id) FROM stdin;
\.


--
-- Name: instrument_id_seq; Type: SEQUENCE SET; Schema: ras_ci; Owner: postgres
--

SELECT pg_catalog.setval('instrument_id_seq', 1, false);


--
-- Data for Name: seft_instrument; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY seft_instrument (id, file_name, data, len, instrument_id) FROM stdin;
\.


--
-- Name: seft_instrument_id_seq; Type: SEQUENCE SET; Schema: ras_ci; Owner: postgres
--

SELECT pg_catalog.setval('seft_instrument_id_seq', 1, false);


--
-- Data for Name: survey; Type: TABLE DATA; Schema: ras_ci; Owner: postgres
--

COPY survey (id, survey_id) FROM stdin;
\.


--
-- Name: survey_id_seq; Type: SEQUENCE SET; Schema: ras_ci; Owner: postgres
--

SELECT pg_catalog.setval('survey_id_seq', 1, false);


SET search_path = sample, pg_catalog;

--
-- Data for Name: collectionexercisejob; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY collectionexercisejob (collectionexercisejobpk, collectionexerciseid, surveyref, exercisedatetime, createddatetime, samplesummaryid) FROM stdin;
\.


--
-- Name: collectionexercisejobseq; Type: SEQUENCE SET; Schema: sample; Owner: samplesvc
--

SELECT pg_catalog.setval('collectionexercisejobseq', 1, false);


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
9.39.0-1	Narinder Birk	database/changes/release-9.39.0/changelog.yml	2018-03-08 15:31:30.533035	1	EXECUTED	7:6afa162d0070b88dadc35457136e9e83	sqlFile		\N	3.5.3	\N	\N	0523090294
9.39.0-2	Narinder Birk	database/changes/release-9.39.0/changelog.yml	2018-03-08 15:31:30.579448	2	EXECUTED	7:4ad80928e62a5579cf15e2f2dfba9940	sqlFile		\N	3.5.3	\N	\N	0523090294
10.43.1	Kieran Wardle	database/changes/release-10.43.0/changelog.yml	2018-03-08 15:31:30.610163	3	EXECUTED	7:8c4084e8becbc263e346e86be6094098	sqlFile		\N	3.5.3	\N	\N	0523090294
10.45.0-1	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:30.636162	4	EXECUTED	7:058cea246265e1cc252fb1b539211646	sqlFile		\N	3.5.3	\N	\N	0523090294
10.45.0-2	Sarah Radford	database/changes/release-10.45.0/changelog.yml	2018-03-08 15:31:30.662444	5	EXECUTED	7:5a68c24a9ed96183a06c3b71e41c8bab	sqlFile		\N	3.5.3	\N	\N	0523090294
10.46.0-1	Sarah Radford	database/changes/release-10.46.0/changelog.yml	2018-03-08 15:31:30.73184	6	EXECUTED	7:cd0f431997b6531bc49f5ca7bb4e871c	sqlFile		\N	3.5.3	\N	\N	0523090294
10.49.0-1	Sarah Radford	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:32:48.479073	7	EXECUTED	7:b8f0c2df73584e8ed4e5bda477f592af	sqlFile		\N	3.5.3	\N	\N	0523168430
10.49.0-2	Kieran Wardle	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:32:48.503111	8	EXECUTED	7:8f841cf4bdfcefb9ae76c037c11e1893	sqlFile		\N	3.5.3	\N	\N	0523168430
10.49.0-3	Edward Stevens	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:32:48.519508	9	EXECUTED	7:ce49882d69211ef1bac74ac847d62e35	sqlFile		\N	3.5.3	\N	\N	0523168430
10.49.0-4	Tejas Patel	database/changes/release-10.49.0/changelog.yml	2018-03-08 15:32:48.526529	10	EXECUTED	7:c294c37a837fffddde7af90f3c30da13	sqlFile		\N	3.5.3	\N	\N	0523168430
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: messagelog; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY messagelog (messagelogpk, messagetext, jobid, messagelevel, functionname, createddatetime) FROM stdin;
\.


--
-- Name: messagelogseq; Type: SEQUENCE SET; Schema: sample; Owner: samplesvc
--

SELECT pg_catalog.setval('messagelogseq', 1, false);


--
-- Data for Name: report; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY report (id, reportpk, reporttypefk, contents, createddatetime) FROM stdin;
\.


--
-- Name: reportpkseq; Type: SEQUENCE SET; Schema: sample; Owner: samplesvc
--

SELECT pg_catalog.setval('reportpkseq', 1, false);


--
-- Data for Name: reporttype; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY reporttype (reporttypepk, displayorder, displayname) FROM stdin;
SAMPLE	20	Sample Units
\.


--
-- Data for Name: samplesummary; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY samplesummary (samplesummarypk, statefk, ingestdatetime, id, description, totalsampleunits, expectedcollectioninstruments) FROM stdin;
\.


--
-- Name: samplesummaryseq; Type: SEQUENCE SET; Schema: sample; Owner: samplesvc
--

SELECT pg_catalog.setval('samplesummaryseq', 1, false);


--
-- Data for Name: samplesummarystate; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY samplesummarystate (statepk) FROM stdin;
INIT
ACTIVE
\.


--
-- Data for Name: sampleunit; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY sampleunit (sampleunitpk, samplesummaryfk, sampleunitref, sampleunittype, formtype, statefk, id) FROM stdin;
\.


--
-- Name: sampleunitseq; Type: SEQUENCE SET; Schema: sample; Owner: samplesvc
--

SELECT pg_catalog.setval('sampleunitseq', 1, false);


--
-- Data for Name: sampleunitstate; Type: TABLE DATA; Schema: sample; Owner: samplesvc
--

COPY sampleunitstate (statepk) FROM stdin;
INIT
DELIVERED
PERSISTED
\.


SET search_path = survey, pg_catalog;

--
-- Data for Name: classifiertype; Type: TABLE DATA; Schema: survey; Owner: postgres
--

COPY classifiertype (classifiertypepk, classifiertypeselectorfk, classifiertype) FROM stdin;
1	1	COLLECTION_EXERCISE
2	1	RU_REF
3	2	LEGAL_BASIS
\.


--
-- Name: classifiertype_classifiertypepk_seq; Type: SEQUENCE SET; Schema: survey; Owner: postgres
--

SELECT pg_catalog.setval('classifiertype_classifiertypepk_seq', 1, false);


--
-- Data for Name: classifiertypeselector; Type: TABLE DATA; Schema: survey; Owner: postgres
--

COPY classifiertypeselector (classifiertypeselectorpk, id, surveyfk, classifiertypeselector) FROM stdin;
1	efa868fb-fb80-44c7-9f33-d6800a17c4da	1	COLLECTION_INSTRUMENT
2	e119ffd6-6fc1-426c-ae81-67a96f9a71ba	1	COMMUNICATION_TEMPLATE
3	f8bb4b96-e63a-11e7-80c1-9a214cf093ae	2	COLLECTION_INSTRUMENT
4	f8bb4ccc-e63a-11e7-80c1-9a214cf093ae	2	COMMUNICATION_TEMPLATE
5	f8bb4a6a-e63a-11e7-80c1-9a214cf093ae	3	COLLECTION_INSTRUMENT
6	f8bb492a-e63a-11e7-80c1-9a214cf093ae	3	COMMUNICATION_TEMPLATE
7	f8bb47cc-e63a-11e7-80c1-9a214cf093ae	4	COLLECTION_INSTRUMENT
8	f8bb44ac-e63a-11e7-80c1-9a214cf093ae	4	COMMUNICATION_TEMPLATE
9	f8bb4380-e63a-11e7-80c1-9a214cf093ae	5	COLLECTION_INSTRUMENT
10	f8bb4254-e63a-11e7-80c1-9a214cf093ae	5	COMMUNICATION_TEMPLATE
11	f8bb4128-e63a-11e7-80c1-9a214cf093ae	6	COLLECTION_INSTRUMENT
12	f8bb3fe8-e63a-11e7-80c1-9a214cf093ae	6	COMMUNICATION_TEMPLATE
13	f8bb3e6c-e63a-11e7-80c1-9a214cf093ae	7	COLLECTION_INSTRUMENT
14	f8bb3ab6-e63a-11e7-80c1-9a214cf093ae	7	COMMUNICATION_TEMPLATE
15	f8bb3980-e63a-11e7-80c1-9a214cf093ae	8	COLLECTION_INSTRUMENT
16	f8bb3840-e63a-11e7-80c1-9a214cf093ae	8	COMMUNICATION_TEMPLATE
17	f8bb361a-e63a-11e7-80c1-9a214cf093ae	9	COLLECTION_INSTRUMENT
18	f8bb34f8-e63a-11e7-80c1-9a214cf093ae	9	COMMUNICATION_TEMPLATE
19	f8bb33c2-e63a-11e7-80c1-9a214cf093ae	10	COLLECTION_INSTRUMENT
20	f8bb326e-e63a-11e7-80c1-9a214cf093ae	10	COMMUNICATION_TEMPLATE
21	f8bb2f1c-e63a-11e7-80c1-9a214cf093ae	11	COLLECTION_INSTRUMENT
22	f8bb2df0-e63a-11e7-80c1-9a214cf093ae	11	COMMUNICATION_TEMPLATE
23	f8bb2cc4-e63a-11e7-80c1-9a214cf093ae	12	COLLECTION_INSTRUMENT
24	f8bb2b84-e63a-11e7-80c1-9a214cf093ae	12	COMMUNICATION_TEMPLATE
25	f8bb27c4-e63a-11e7-80c1-9a214cf093ae	13	COLLECTION_INSTRUMENT
26	f8bb2698-e63a-11e7-80c1-9a214cf093ae	13	COMMUNICATION_TEMPLATE
27	f8bb256c-e63a-11e7-80c1-9a214cf093ae	14	COLLECTION_INSTRUMENT
28	f8bb2422-e63a-11e7-80c1-9a214cf093ae	14	COMMUNICATION_TEMPLATE
29	f8bb2184-e63a-11e7-80c1-9a214cf093ae	15	COLLECTION_INSTRUMENT
30	f8bb2044-e63a-11e7-80c1-9a214cf093ae	15	COMMUNICATION_TEMPLATE
31	f8bb1efa-e63a-11e7-80c1-9a214cf093ae	16	COLLECTION_INSTRUMENT
32	f8bb1c52-e63a-11e7-80c1-9a214cf093ae	16	COMMUNICATION_TEMPLATE
\.


--
-- Name: classifiertypeselector_classifiertypeselectorpk_seq; Type: SEQUENCE SET; Schema: survey; Owner: postgres
--

SELECT pg_catalog.setval('classifiertypeselector_classifiertypeselectorpk_seq', 1, false);


--
-- Data for Name: survey; Type: TABLE DATA; Schema: survey; Owner: postgres
--

COPY survey (surveypk, id, shortname, longname, surveyref, legalbasis) FROM stdin;
1	cb0711c3-0ac8-41d3-ae0e-567e5ea1ef87	BRES	Business Register and Employment Survey	221	Statistics of Trade Act 1947
2	75b19ea0-69a4-4c58-8d7f-4458c8f43f5c	RSI	Monthly Business Survey - Retail Sales Index	023	Statistics of Trade Act 1947
3	41320b22-b425-4fba-a90e-718898f718ce	AIFDI	Annual Inward Foreign Direct Investment Survey	062	Statistics of Trade Act 1947
4	04dbb407-4438-4f89-acc4-53445d75330c	AOFDI	Annual Outward Foreign Direct Investment Survey	063	Statistics of Trade Act 1947
5	c3eaeff3-d570-475d-9859-32c3bf87800d	QIFDI	Quarterly Inward Foreign Direct Investment Survey	064	Statistics of Trade Act 1947
6	57a43c94-9f81-4f33-bad8-f94800a66503	QOFDI	Quarterly Outward Foreign Direct Investment Survey	065	Statistics of Trade Act 1947
7	c48d6646-eb6f-4c7c-9f37-f7b41c8d2bc6	Sand&Gravel	Quarterly Survey of Building Materials Sand and Gravel	066	Statistics of Trade Act 1947 - BEIS
8	9b6872eb-28ee-4c09-b705-c3ab1bb0f9ec	Blocks	Monthly Survey of Building Materials Concrete Building Blocks	073	Statistics of Trade Act 1947 - BEIS
9	cb8accda-6118-4d3b-85a3-149e28960c54	Bricks	Monthly Survey of Building Materials Bricks	074	Voluntary - BEIS
10	c23bb1c1-5202-43bb-8357-7a07c844308f	MWSS	Monthly Wages and Salaries Survey	134	Statistics of Trade Act 1947
11	416b8a82-2031-4f41-b59b-95482d916ca3	PCS	Public Corporations Survey	137	Voluntary Not Stated
12	02b9c366-7397-42f7-942a-76dc5876d86d	QBS	Quarterly Business Survey	139	Statistics of Trade Act 1947
13	6aa8896f-ced5-4694-800c-6cd661b0c8b2	ASHE	Annual Survey of Hours and Earnings	141	Statistics of Trade Act 1947
14	7a2c9d6c-9aaf-4cf0-a68c-1d50b3f1b296	NBS	National Balance Sheet	199	Voluntary Not Stated
15	0fc6fa22-8938-43b6-81c5-f1ccca5a5494	OFATS	Outward Foreign Affiliates Statistics Survey	225	Statistics of Trade Act 1947
16	a81f8a72-47e1-4fcf-a88b-0c175829e02b	GovERD	Government Research and Development Survey	500	GovERD
\.


--
-- Name: survey_surveypk_seq; Type: SEQUENCE SET; Schema: survey; Owner: postgres
--

SELECT pg_catalog.setval('survey_surveypk_seq', 1, false);


SET search_path = templatesvc, pg_catalog;

--
-- Data for Name: classificationtype; Type: TABLE DATA; Schema: templatesvc; Owner: postgres
--

COPY classificationtype (name) FROM stdin;
\.


--
-- Data for Name: template; Type: TABLE DATA; Schema: templatesvc; Owner: postgres
--

COPY template (id, label, type, uri, classification, params) FROM stdin;
\.


SET search_path = action, pg_catalog;

--
-- Name: action actionid_uuid_key; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY action
    ADD CONSTRAINT actionid_uuid_key UNIQUE (id);


--
-- Name: action actionpk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY action
    ADD CONSTRAINT actionpk_pkey PRIMARY KEY (actionpk);


--
-- Name: actionplan actionplanid_uuid_key; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplan
    ADD CONSTRAINT actionplanid_uuid_key UNIQUE (id);


--
-- Name: actionplanjob actionplanjobid_uuid_key; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplanjob
    ADD CONSTRAINT actionplanjobid_uuid_key UNIQUE (id);


--
-- Name: actionplanjob actionplanjobpk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplanjob
    ADD CONSTRAINT actionplanjobpk_pkey PRIMARY KEY (actionplanjobpk);


--
-- Name: actionplan actionplanpk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplan
    ADD CONSTRAINT actionplanpk_pkey PRIMARY KEY (actionplanpk);


--
-- Name: actionrule actionrulepk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionrule
    ADD CONSTRAINT actionrulepk_pkey PRIMARY KEY (actionrulepk);


--
-- Name: actionstate actionstatepk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionstate
    ADD CONSTRAINT actionstatepk_pkey PRIMARY KEY (statepk);


--
-- Name: actiontype actiontypepk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actiontype
    ADD CONSTRAINT actiontypepk_pkey PRIMARY KEY (actiontypepk);


--
-- Name: case caseid_uuid_key; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY "case"
    ADD CONSTRAINT caseid_uuid_key UNIQUE (id);


--
-- Name: case casepk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY "case"
    ADD CONSTRAINT casepk_pkey PRIMARY KEY (casepk);


--
-- Name: messagelog messagepk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY messagelog
    ADD CONSTRAINT messagepk_pkey PRIMARY KEY (messagepk);


--
-- Name: actionplan name_key; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplan
    ADD CONSTRAINT name_key UNIQUE (name);


--
-- Name: outcomecategory outcomecategory_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY outcomecategory
    ADD CONSTRAINT outcomecategory_pkey PRIMARY KEY (handlerpk, actionoutcomepk);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


--
-- Name: report report_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_pkey PRIMARY KEY (reportpk);


--
-- Name: report report_uuid_key; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_uuid_key UNIQUE (id);


--
-- Name: reporttype reporttype_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY reporttype
    ADD CONSTRAINT reporttype_pkey PRIMARY KEY (reporttypepk);


--
-- Name: actionplanjobstate statepk_pkey; Type: CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplanjobstate
    ADD CONSTRAINT statepk_pkey PRIMARY KEY (statepk);


SET search_path = actionexporter, pg_catalog;

--
-- Name: actionrequest actionrequestpk_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY actionrequest
    ADD CONSTRAINT actionrequestpk_pkey PRIMARY KEY (actionrequestpk);


--
-- Name: templatemapping actiontypenamepk_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY templatemapping
    ADD CONSTRAINT actiontypenamepk_pkey PRIMARY KEY (actiontypenamepk);


--
-- Name: contact contactpk_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY contact
    ADD CONSTRAINT contactpk_pkey PRIMARY KEY (contactpk);


--
-- Name: messagelog messagepk_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY messagelog
    ADD CONSTRAINT messagepk_pkey PRIMARY KEY (messagepk);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


--
-- Name: report report_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_pkey PRIMARY KEY (reportpk);


--
-- Name: report report_uuid_key; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_uuid_key UNIQUE (id);


--
-- Name: reporttype reporttype_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY reporttype
    ADD CONSTRAINT reporttype_pkey PRIMARY KEY (reporttypepk);


--
-- Name: address sampleunitrefpk_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY address
    ADD CONSTRAINT sampleunitrefpk_pkey PRIMARY KEY (sampleunitrefpk);


--
-- Name: template templetenamepk_pkey; Type: CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY template
    ADD CONSTRAINT templetenamepk_pkey PRIMARY KEY (templatenamepk);


SET search_path = casesvc, pg_catalog;

--
-- Name: case case_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY "case"
    ADD CONSTRAINT case_pkey PRIMARY KEY (casepk);


--
-- Name: case case_uuid_key; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY "case"
    ADD CONSTRAINT case_uuid_key UNIQUE (id);


--
-- Name: caseevent caseevent_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY caseevent
    ADD CONSTRAINT caseevent_pkey PRIMARY KEY (caseeventpk);


--
-- Name: casegroup casegroup_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY casegroup
    ADD CONSTRAINT casegroup_pkey PRIMARY KEY (casegrouppk);


--
-- Name: casegroup casegroup_uuid_key; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY casegroup
    ADD CONSTRAINT casegroup_uuid_key UNIQUE (id);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_pkey PRIMARY KEY (categorypk);


--
-- Name: messagelog messagelogpk_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY messagelog
    ADD CONSTRAINT messagelogpk_pkey PRIMARY KEY (messagelogpk);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


--
-- Name: report report_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_pkey PRIMARY KEY (reportpk);


--
-- Name: report report_uuid_key; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_uuid_key UNIQUE (id);


--
-- Name: reporttype reporttype_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY reporttype
    ADD CONSTRAINT reporttype_pkey PRIMARY KEY (reporttypepk);


--
-- Name: response response_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY response
    ADD CONSTRAINT response_pkey PRIMARY KEY (responsepk);


--
-- Name: casestate state_pkey; Type: CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY casestate
    ADD CONSTRAINT state_pkey PRIMARY KEY (statepk);


SET search_path = collectionexercise, pg_catalog;

--
-- Name: casetypedefault casetypedefaultpk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY casetypedefault
    ADD CONSTRAINT casetypedefaultpk_pkey PRIMARY KEY (casetypedefaultpk);


--
-- Name: casetypeoverride casetypeoverridepk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY casetypeoverride
    ADD CONSTRAINT casetypeoverridepk_pkey PRIMARY KEY (casetypeoverridepk);


--
-- Name: collectionexercise ce_id_uuid_key; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY collectionexercise
    ADD CONSTRAINT ce_id_uuid_key UNIQUE (id);


--
-- Name: collectionexercisestate collectionexercise_statepk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY collectionexercisestate
    ADD CONSTRAINT collectionexercise_statepk_pkey PRIMARY KEY (statepk);


--
-- Name: event event_collexfk_tag_key; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_collexfk_tag_key UNIQUE (collexfk, tag);


--
-- Name: event event_id_key; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_id_key UNIQUE (id);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_pkey PRIMARY KEY (eventpk);


--
-- Name: collectionexercise exercisepk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY collectionexercise
    ADD CONSTRAINT exercisepk_pkey PRIMARY KEY (exercisepk);


--
-- Name: messagelog messagelogpk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY messagelog
    ADD CONSTRAINT messagelogpk_pkey PRIMARY KEY (messagelogpk);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


--
-- Name: report report_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_pkey PRIMARY KEY (reportpk);


--
-- Name: report report_uuid_key; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_uuid_key UNIQUE (id);


--
-- Name: reporttype reporttype_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY reporttype
    ADD CONSTRAINT reporttype_pkey PRIMARY KEY (reporttypepk);


--
-- Name: samplelink samplelinkpk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY samplelink
    ADD CONSTRAINT samplelinkpk_pkey PRIMARY KEY (samplelinkpk);


--
-- Name: sampleunitgroupstate sampleunitgroup_statepk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunitgroupstate
    ADD CONSTRAINT sampleunitgroup_statepk_pkey PRIMARY KEY (statepk);


--
-- Name: sampleunitgroup sampleunitgrouppk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunitgroup
    ADD CONSTRAINT sampleunitgrouppk_pkey PRIMARY KEY (sampleunitgrouppk);


--
-- Name: sampleunit sampleunitpk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunit
    ADD CONSTRAINT sampleunitpk_pkey PRIMARY KEY (sampleunitpk);


--
-- Name: sampleunittype sampleunittypepk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunittype
    ADD CONSTRAINT sampleunittypepk_pkey PRIMARY KEY (sampleunittypepk);


--
-- Name: survey survey_id_uuid_key; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY survey
    ADD CONSTRAINT survey_id_uuid_key UNIQUE (id);


--
-- Name: survey surveypk_pkey; Type: CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY survey
    ADD CONSTRAINT surveypk_pkey PRIMARY KEY (surveypk);


SET search_path = iac, pg_catalog;

--
-- Name: iac code_pkey; Type: CONSTRAINT; Schema: iac; Owner: postgres
--

ALTER TABLE ONLY iac
    ADD CONSTRAINT code_pkey PRIMARY KEY (code);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: iac; Owner: postgres
--

ALTER TABLE ONLY databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


SET search_path = notifygatewaysvc, pg_catalog;

--
-- Name: message message_pkey; Type: CONSTRAINT; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

ALTER TABLE ONLY message
    ADD CONSTRAINT message_pkey PRIMARY KEY (messagepk);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

ALTER TABLE ONLY databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


SET search_path = partysvc, pg_catalog;

--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: business_attributes business_attributes_pkey; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business_attributes
    ADD CONSTRAINT business_attributes_pkey PRIMARY KEY (id);


--
-- Name: business business_business_ref_key; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business
    ADD CONSTRAINT business_business_ref_key UNIQUE (business_ref);


--
-- Name: business business_pkey; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business
    ADD CONSTRAINT business_pkey PRIMARY KEY (party_uuid);


--
-- Name: business_respondent business_respondent_pkey; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business_respondent
    ADD CONSTRAINT business_respondent_pkey PRIMARY KEY (business_id, respondent_id);


--
-- Name: enrolment enrolment_pkey; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY enrolment
    ADD CONSTRAINT enrolment_pkey PRIMARY KEY (business_id, respondent_id, survey_id);


--
-- Name: pending_enrolment pending_enrolment_pkey; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY pending_enrolment
    ADD CONSTRAINT pending_enrolment_pkey PRIMARY KEY (id);


--
-- Name: respondent respondent_email_address_key; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY respondent
    ADD CONSTRAINT respondent_email_address_key UNIQUE (email_address);


--
-- Name: respondent respondent_party_uuid_key; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY respondent
    ADD CONSTRAINT respondent_party_uuid_key UNIQUE (party_uuid);


--
-- Name: respondent respondent_pkey; Type: CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY respondent
    ADD CONSTRAINT respondent_pkey PRIMARY KEY (id);


SET search_path = public, pg_catalog;

--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: credentials_oauthclient credentials_oauthclient_client_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY credentials_oauthclient
    ADD CONSTRAINT credentials_oauthclient_client_id_key UNIQUE (client_id);


--
-- Name: credentials_oauthclient credentials_oauthclient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY credentials_oauthclient
    ADD CONSTRAINT credentials_oauthclient_pkey PRIMARY KEY (id);


--
-- Name: credentials_oauthuser credentials_oauthuser_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY credentials_oauthuser
    ADD CONSTRAINT credentials_oauthuser_email_key UNIQUE (email);


--
-- Name: credentials_oauthuser credentials_oauthuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY credentials_oauthuser
    ADD CONSTRAINT credentials_oauthuser_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: expiring_code_store expiring_code_store_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY expiring_code_store
    ADD CONSTRAINT expiring_code_store_pkey PRIMARY KEY (code);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: identity_provider identity_provider_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY identity_provider
    ADD CONSTRAINT identity_provider_pkey PRIMARY KEY (id);


--
-- Name: identity_zone identity_zone_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY identity_zone
    ADD CONSTRAINT identity_zone_pkey PRIMARY KEY (id);


--
-- Name: mfa_providers mfa_providers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY mfa_providers
    ADD CONSTRAINT mfa_providers_pkey PRIMARY KEY (id);


--
-- Name: authz_approvals new_authz_approvals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY authz_approvals
    ADD CONSTRAINT new_authz_approvals_pkey PRIMARY KEY (user_id, client_id, scope);


--
-- Name: oauth_client_details oauth_client_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY oauth_client_details
    ADD CONSTRAINT oauth_client_details_pkey PRIMARY KEY (client_id, identity_zone_id);


--
-- Name: revocable_tokens revocable_tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY revocable_tokens
    ADD CONSTRAINT revocable_tokens_pkey PRIMARY KEY (token_id);


--
-- Name: schema_version schema_version_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY schema_version
    ADD CONSTRAINT schema_version_pk PRIMARY KEY (installed_rank);


--
-- Name: service_provider service_provider_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY service_provider
    ADD CONSTRAINT service_provider_pkey PRIMARY KEY (id);


--
-- Name: tokens_oauthaccesstoken tokens_oauthaccesstoken_access_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken
    ADD CONSTRAINT tokens_oauthaccesstoken_access_token_key UNIQUE (access_token);


--
-- Name: tokens_oauthaccesstoken tokens_oauthaccesstoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken
    ADD CONSTRAINT tokens_oauthaccesstoken_pkey PRIMARY KEY (id);


--
-- Name: tokens_oauthaccesstoken tokens_oauthaccesstoken_refresh_token_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken
    ADD CONSTRAINT tokens_oauthaccesstoken_refresh_token_id_key UNIQUE (refresh_token_id);


--
-- Name: tokens_oauthaccesstoken_scopes tokens_oauthaccesstoken_scope_oauthaccesstoken_id_1497353e_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken_scopes
    ADD CONSTRAINT tokens_oauthaccesstoken_scope_oauthaccesstoken_id_1497353e_uniq UNIQUE (oauthaccesstoken_id, oauthscope_id);


--
-- Name: tokens_oauthaccesstoken_scopes tokens_oauthaccesstoken_scopes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken_scopes
    ADD CONSTRAINT tokens_oauthaccesstoken_scopes_pkey PRIMARY KEY (id);


--
-- Name: tokens_oauthauthorizationcode_scopes tokens_oauthauthorizati_oauthauthorizationcode_id_28200133_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode_scopes
    ADD CONSTRAINT tokens_oauthauthorizati_oauthauthorizationcode_id_28200133_uniq UNIQUE (oauthauthorizationcode_id, oauthscope_id);


--
-- Name: tokens_oauthauthorizationcode tokens_oauthauthorizationcode_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode
    ADD CONSTRAINT tokens_oauthauthorizationcode_code_key UNIQUE (code);


--
-- Name: tokens_oauthauthorizationcode tokens_oauthauthorizationcode_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode
    ADD CONSTRAINT tokens_oauthauthorizationcode_pkey PRIMARY KEY (id);


--
-- Name: tokens_oauthauthorizationcode_scopes tokens_oauthauthorizationcode_scopes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode_scopes
    ADD CONSTRAINT tokens_oauthauthorizationcode_scopes_pkey PRIMARY KEY (id);


--
-- Name: tokens_oauthrefreshtoken tokens_oauthrefreshtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthrefreshtoken
    ADD CONSTRAINT tokens_oauthrefreshtoken_pkey PRIMARY KEY (id);


--
-- Name: tokens_oauthrefreshtoken tokens_oauthrefreshtoken_refresh_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthrefreshtoken
    ADD CONSTRAINT tokens_oauthrefreshtoken_refresh_token_key UNIQUE (refresh_token);


--
-- Name: tokens_oauthscope tokens_oauthscope_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthscope
    ADD CONSTRAINT tokens_oauthscope_pkey PRIMARY KEY (id);


--
-- Name: tokens_oauthscope tokens_oauthscope_scope_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthscope
    ADD CONSTRAINT tokens_oauthscope_scope_key UNIQUE (scope);


--
-- Name: user_google_mfa_credentials user_google_mfa_credentials_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY user_google_mfa_credentials
    ADD CONSTRAINT user_google_mfa_credentials_pkey PRIMARY KEY (user_id, mfa_provider_id);


--
-- Name: user_info user_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY user_info
    ADD CONSTRAINT user_info_pkey PRIMARY KEY (user_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


SET search_path = ras_ci, pg_catalog;

--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: business business_pkey; Type: CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY business
    ADD CONSTRAINT business_pkey PRIMARY KEY (id);


--
-- Name: exercise exercise_pkey; Type: CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY exercise
    ADD CONSTRAINT exercise_pkey PRIMARY KEY (id);


--
-- Name: instrument instrument_pkey; Type: CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY instrument
    ADD CONSTRAINT instrument_pkey PRIMARY KEY (id);


--
-- Name: seft_instrument seft_instrument_pkey; Type: CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY seft_instrument
    ADD CONSTRAINT seft_instrument_pkey PRIMARY KEY (id);


--
-- Name: survey survey_pkey; Type: CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY survey
    ADD CONSTRAINT survey_pkey PRIMARY KEY (id);


SET search_path = sample, pg_catalog;

--
-- Name: collectionexercisejob collectionexercisejob_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY collectionexercisejob
    ADD CONSTRAINT collectionexercisejob_pkey PRIMARY KEY (collectionexercisejobpk);


--
-- Name: messagelog messagelogpk_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY messagelog
    ADD CONSTRAINT messagelogpk_pkey PRIMARY KEY (messagelogpk);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


--
-- Name: report report_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_pkey PRIMARY KEY (reportpk);


--
-- Name: report report_uuid_key; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT report_uuid_key UNIQUE (id);


--
-- Name: reporttype reporttype_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY reporttype
    ADD CONSTRAINT reporttype_pkey PRIMARY KEY (reporttypepk);


--
-- Name: samplesummary samplesummary_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY samplesummary
    ADD CONSTRAINT samplesummary_pkey PRIMARY KEY (samplesummarypk);


--
-- Name: samplesummary samplesummary_uuid_key; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY samplesummary
    ADD CONSTRAINT samplesummary_uuid_key UNIQUE (id);


--
-- Name: samplesummarystate samplesummarystate_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY samplesummarystate
    ADD CONSTRAINT samplesummarystate_pkey PRIMARY KEY (statepk);


--
-- Name: sampleunit sampleunit_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY sampleunit
    ADD CONSTRAINT sampleunit_pkey PRIMARY KEY (sampleunitpk);


--
-- Name: sampleunit sampleunit_uuid_key; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY sampleunit
    ADD CONSTRAINT sampleunit_uuid_key UNIQUE (id);


--
-- Name: sampleunitstate sampleunitstate_pkey; Type: CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY sampleunitstate
    ADD CONSTRAINT sampleunitstate_pkey PRIMARY KEY (statepk);


SET search_path = survey, pg_catalog;

--
-- Name: classifiertype classifiertype_pkey; Type: CONSTRAINT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY classifiertype
    ADD CONSTRAINT classifiertype_pkey PRIMARY KEY (classifiertypepk);


--
-- Name: classifiertypeselector classifiertypeselector_id_key; Type: CONSTRAINT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY classifiertypeselector
    ADD CONSTRAINT classifiertypeselector_id_key UNIQUE (id);


--
-- Name: classifiertypeselector classifiertypeselector_pkey; Type: CONSTRAINT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY classifiertypeselector
    ADD CONSTRAINT classifiertypeselector_pkey PRIMARY KEY (classifiertypeselectorpk);


--
-- Name: survey survey_id_key; Type: CONSTRAINT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY survey
    ADD CONSTRAINT survey_id_key UNIQUE (id);


--
-- Name: survey survey_pkey; Type: CONSTRAINT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY survey
    ADD CONSTRAINT survey_pkey PRIMARY KEY (surveypk);


SET search_path = templatesvc, pg_catalog;

--
-- Name: classificationtype classificationtype_pkey; Type: CONSTRAINT; Schema: templatesvc; Owner: postgres
--

ALTER TABLE ONLY classificationtype
    ADD CONSTRAINT classificationtype_pkey PRIMARY KEY (name);


--
-- Name: template template_pkey; Type: CONSTRAINT; Schema: templatesvc; Owner: postgres
--

ALTER TABLE ONLY template
    ADD CONSTRAINT template_pkey PRIMARY KEY (id);


SET search_path = action, pg_catalog;

--
-- Name: action_actionplanfk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX action_actionplanfk_index ON action USING btree (actionplanfk);


--
-- Name: action_actionrulefk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX action_actionrulefk_index ON action USING btree (actionrulefk);


--
-- Name: action_actiontypefk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX action_actiontypefk_index ON action USING btree (actiontypefk);


--
-- Name: action_optlockversion_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX action_optlockversion_index ON action USING btree (optlockversion);


--
-- Name: action_statefk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX action_statefk_index ON action USING btree (statefk);


--
-- Name: actionplanjob_actionplanfk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX actionplanjob_actionplanfk_index ON actionplanjob USING btree (actionplanfk);


--
-- Name: actionplanjob_statefk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX actionplanjob_statefk_index ON actionplanjob USING btree (statefk);


--
-- Name: actionrule_actionplanfk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX actionrule_actionplanfk_index ON actionrule USING btree (actionplanfk);


--
-- Name: actionrule_actiontypefk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX actionrule_actiontypefk_index ON actionrule USING btree (actiontypefk);


--
-- Name: actiontype_name_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX actiontype_name_index ON actiontype USING btree (name);


--
-- Name: case_actionplanfk_index; Type: INDEX; Schema: action; Owner: actionsvc
--

CREATE INDEX case_actionplanfk_index ON "case" USING btree (actionplanfk);


SET search_path = actionexporter, pg_catalog;

--
-- Name: actionrequest_contactfk_index; Type: INDEX; Schema: actionexporter; Owner: actionexportersvc
--

CREATE INDEX actionrequest_contactfk_index ON actionrequest USING btree (contactfk);


--
-- Name: actionrequest_sampleunitreffk_index; Type: INDEX; Schema: actionexporter; Owner: actionexportersvc
--

CREATE INDEX actionrequest_sampleunitreffk_index ON actionrequest USING btree (sampleunitreffk);


--
-- Name: templatemapping_templatenamefk_index; Type: INDEX; Schema: actionexporter; Owner: actionexportersvc
--

CREATE INDEX templatemapping_templatenamefk_index ON templatemapping USING btree (templatenamefk);


SET search_path = casesvc, pg_catalog;

--
-- Name: case_casegroupfk_index; Type: INDEX; Schema: casesvc; Owner: casesvc
--

CREATE INDEX case_casegroupfk_index ON "case" USING btree (casegroupfk);


--
-- Name: case_state_index; Type: INDEX; Schema: casesvc; Owner: casesvc
--

CREATE INDEX case_state_index ON "case" USING btree (statefk);


--
-- Name: caseevent_casefk_index; Type: INDEX; Schema: casesvc; Owner: casesvc
--

CREATE INDEX caseevent_casefk_index ON caseevent USING btree (casefk);


--
-- Name: caseevent_categoryfk_index; Type: INDEX; Schema: casesvc; Owner: casesvc
--

CREATE INDEX caseevent_categoryfk_index ON caseevent USING btree (categoryfk);


--
-- Name: response_casefk_index; Type: INDEX; Schema: casesvc; Owner: casesvc
--

CREATE INDEX response_casefk_index ON response USING btree (casefk);


SET search_path = collectionexercise, pg_catalog;

--
-- Name: collectionexercise_statefk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX collectionexercise_statefk_index ON collectionexercise USING btree (statefk);


--
-- Name: ctd_sampleunittypefk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX ctd_sampleunittypefk_index ON casetypedefault USING btree (sampleunittypefk);


--
-- Name: cto_exercisefk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX cto_exercisefk_index ON casetypeoverride USING btree (exercisefk);


--
-- Name: cto_sampleunittypefk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX cto_sampleunittypefk_index ON casetypeoverride USING btree (sampleunittypefk);


--
-- Name: sampleunit_sampleunitgroupfk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX sampleunit_sampleunitgroupfk_index ON sampleunit USING btree (sampleunitgroupfk);


--
-- Name: sampleunit_sampleunittypefk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX sampleunit_sampleunittypefk_index ON sampleunit USING btree (sampleunittypefk);


--
-- Name: sampleunitgroup_exercisefk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX sampleunitgroup_exercisefk_index ON sampleunitgroup USING btree (exercisefk);


--
-- Name: sampleunitgroup_statefk_index; Type: INDEX; Schema: collectionexercise; Owner: collectionexercisesvc
--

CREATE INDEX sampleunitgroup_statefk_index ON sampleunitgroup USING btree (statefk);


SET search_path = notifygatewaysvc, pg_catalog;

--
-- Name: message_id_idx; Type: INDEX; Schema: notifygatewaysvc; Owner: notifygatewaysvc
--

CREATE UNIQUE INDEX message_id_idx ON message USING btree (id);


SET search_path = public, pg_catalog;

--
-- Name: audit_created; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX audit_created ON sec_audit USING btree (created);


--
-- Name: audit_principal; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX audit_principal ON sec_audit USING btree (principal_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: credentials_oauthclient_client_id_270ae079_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX credentials_oauthclient_client_id_270ae079_like ON credentials_oauthclient USING btree (client_id varchar_pattern_ops);


--
-- Name: credentials_oauthuser_email_3d9493c5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX credentials_oauthuser_email_3d9493c5_like ON credentials_oauthuser USING btree (email varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: entity_in_zone; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX entity_in_zone ON service_provider USING btree (identity_zone_id, entity_id);


--
-- Name: external_group_unique_key; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX external_group_unique_key ON external_group_mapping USING btree (origin, external_group, group_id);


--
-- Name: group_membership_perf_group_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX group_membership_perf_group_idx ON group_membership USING btree (group_id);


--
-- Name: group_membership_perf_group_lower_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX group_membership_perf_group_lower_idx ON group_membership USING btree (lower((group_id)::text));


--
-- Name: group_membership_perf_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX group_membership_perf_idx ON group_membership USING btree (lower((member_id)::text));


--
-- Name: group_membership_unique_key; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX group_membership_unique_key ON group_membership USING btree (member_id, group_id);


--
-- Name: groups_unique_key; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX groups_unique_key ON groups USING btree (displayname, identity_zone_id);


--
-- Name: groups_unique_lower_key; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX groups_unique_lower_key ON groups USING btree (lower((displayname)::text), lower((identity_zone_id)::text));


--
-- Name: idx_mfa_unique_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_mfa_unique_name ON mfa_providers USING btree (identity_zone_id, lower((name)::text));


--
-- Name: idx_revocable_token_client_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_revocable_token_client_id ON revocable_tokens USING btree (client_id);


--
-- Name: idx_revocable_token_expires_at; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_revocable_token_expires_at ON revocable_tokens USING btree (expires_at);


--
-- Name: idx_revocable_token_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_revocable_token_user_id ON revocable_tokens USING btree (user_id);


--
-- Name: key_in_zone; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX key_in_zone ON identity_provider USING btree (identity_zone_id, origin_key);


--
-- Name: oauth_code_expiresat_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth_code_expiresat_idx ON oauth_code USING btree (expiresat);


--
-- Name: oauth_code_uq_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX oauth_code_uq_idx ON oauth_code USING btree (code);


--
-- Name: revocable_tokens_zone_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX revocable_tokens_zone_id ON revocable_tokens USING btree (identity_zone_id);


--
-- Name: schema_version_s_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX schema_version_s_idx ON schema_version USING btree (success);


--
-- Name: sec_audit_created_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sec_audit_created_idx ON sec_audit USING btree (created);


--
-- Name: sec_audit_principal_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sec_audit_principal_idx ON sec_audit USING btree (principal_id);


--
-- Name: subdomain; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX subdomain ON identity_zone USING btree (subdomain);


--
-- Name: tokens_oauthaccesstoken_2bfe9d72; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthaccesstoken_2bfe9d72 ON tokens_oauthaccesstoken USING btree (client_id);


--
-- Name: tokens_oauthaccesstoken_access_token_0ca96316_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthaccesstoken_access_token_0ca96316_like ON tokens_oauthaccesstoken USING btree (access_token varchar_pattern_ops);


--
-- Name: tokens_oauthaccesstoken_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthaccesstoken_e8701ad4 ON tokens_oauthaccesstoken USING btree (user_id);


--
-- Name: tokens_oauthaccesstoken_scopes_6e643d1e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthaccesstoken_scopes_6e643d1e ON tokens_oauthaccesstoken_scopes USING btree (oauthscope_id);


--
-- Name: tokens_oauthaccesstoken_scopes_713369b6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthaccesstoken_scopes_713369b6 ON tokens_oauthaccesstoken_scopes USING btree (oauthaccesstoken_id);


--
-- Name: tokens_oauthauthorizationcode_2bfe9d72; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthauthorizationcode_2bfe9d72 ON tokens_oauthauthorizationcode USING btree (client_id);


--
-- Name: tokens_oauthauthorizationcode_code_36706cec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthauthorizationcode_code_36706cec_like ON tokens_oauthauthorizationcode USING btree (code varchar_pattern_ops);


--
-- Name: tokens_oauthauthorizationcode_e8701ad4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthauthorizationcode_e8701ad4 ON tokens_oauthauthorizationcode USING btree (user_id);


--
-- Name: tokens_oauthauthorizationcode_scopes_6e643d1e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthauthorizationcode_scopes_6e643d1e ON tokens_oauthauthorizationcode_scopes USING btree (oauthscope_id);


--
-- Name: tokens_oauthauthorizationcode_scopes_9050429e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthauthorizationcode_scopes_9050429e ON tokens_oauthauthorizationcode_scopes USING btree (oauthauthorizationcode_id);


--
-- Name: tokens_oauthrefreshtoken_refresh_token_c8ea33b6_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthrefreshtoken_refresh_token_c8ea33b6_like ON tokens_oauthrefreshtoken USING btree (refresh_token varchar_pattern_ops);


--
-- Name: tokens_oauthscope_scope_3bf35d98_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX tokens_oauthscope_scope_3bf35d98_like ON tokens_oauthscope USING btree (scope varchar_pattern_ops);


--
-- Name: user_identity_zone; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_identity_zone ON users USING btree (identity_zone_id);


--
-- Name: user_perf_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_perf_email ON users USING btree (lower((email)::text));


--
-- Name: user_perf_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_perf_id ON users USING btree (lower((id)::text));


--
-- Name: users_unique_key; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX users_unique_key ON users USING btree (origin, lower((username)::text), identity_zone_id);


SET search_path = ras_ci, pg_catalog;

--
-- Name: ix_business_ru_ref; Type: INDEX; Schema: ras_ci; Owner: postgres
--

CREATE INDEX ix_business_ru_ref ON business USING btree (ru_ref);


--
-- Name: ix_exercise_exercise_id; Type: INDEX; Schema: ras_ci; Owner: postgres
--

CREATE INDEX ix_exercise_exercise_id ON exercise USING btree (exercise_id);


--
-- Name: ix_instrument_instrument_id; Type: INDEX; Schema: ras_ci; Owner: postgres
--

CREATE UNIQUE INDEX ix_instrument_instrument_id ON instrument USING btree (instrument_id);


--
-- Name: ix_survey_survey_id; Type: INDEX; Schema: ras_ci; Owner: postgres
--

CREATE INDEX ix_survey_survey_id ON survey USING btree (survey_id);


SET search_path = sample, pg_catalog;

--
-- Name: samplesummary_statefk_index; Type: INDEX; Schema: sample; Owner: samplesvc
--

CREATE INDEX samplesummary_statefk_index ON samplesummary USING btree (statefk);


--
-- Name: sampleunit_samplesummaryfk_index; Type: INDEX; Schema: sample; Owner: samplesvc
--

CREATE INDEX sampleunit_samplesummaryfk_index ON sampleunit USING btree (samplesummaryfk);


--
-- Name: sampleunit_statefk_index; Type: INDEX; Schema: sample; Owner: samplesvc
--

CREATE INDEX sampleunit_statefk_index ON sampleunit USING btree (statefk);


SET search_path = action, pg_catalog;

--
-- Name: actionplanjob actionplanfk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplanjob
    ADD CONSTRAINT actionplanfk_fkey FOREIGN KEY (actionplanfk) REFERENCES actionplan(actionplanpk);


--
-- Name: action actionplanfk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY action
    ADD CONSTRAINT actionplanfk_fkey FOREIGN KEY (actionplanfk) REFERENCES actionplan(actionplanpk);


--
-- Name: actionrule actionplanfk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionrule
    ADD CONSTRAINT actionplanfk_fkey FOREIGN KEY (actionplanfk) REFERENCES actionplan(actionplanpk);


--
-- Name: case actionplanfk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY "case"
    ADD CONSTRAINT actionplanfk_fkey FOREIGN KEY (actionplanfk) REFERENCES actionplan(actionplanpk);


--
-- Name: actionplanjob actionplanjobstate_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionplanjob
    ADD CONSTRAINT actionplanjobstate_fkey FOREIGN KEY (statefk) REFERENCES actionplanjobstate(statepk);


--
-- Name: action actionrulefk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY action
    ADD CONSTRAINT actionrulefk_fkey FOREIGN KEY (actionrulefk) REFERENCES actionrule(actionrulepk);


--
-- Name: action actionstatefk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY action
    ADD CONSTRAINT actionstatefk_fkey FOREIGN KEY (statefk) REFERENCES actionstate(statepk);


--
-- Name: action actiontypefk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY action
    ADD CONSTRAINT actiontypefk_fkey FOREIGN KEY (actiontypefk) REFERENCES actiontype(actiontypepk);


--
-- Name: actionrule actiontypefk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY actionrule
    ADD CONSTRAINT actiontypefk_fkey FOREIGN KEY (actiontypefk) REFERENCES actiontype(actiontypepk);


--
-- Name: report reporttypefk_fkey; Type: FK CONSTRAINT; Schema: action; Owner: actionsvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT reporttypefk_fkey FOREIGN KEY (reporttypefk) REFERENCES reporttype(reporttypepk);


SET search_path = actionexporter, pg_catalog;

--
-- Name: actionrequest contactfk_fkey; Type: FK CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY actionrequest
    ADD CONSTRAINT contactfk_fkey FOREIGN KEY (contactfk) REFERENCES contact(contactpk);


--
-- Name: report reporttypefk_fkey; Type: FK CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT reporttypefk_fkey FOREIGN KEY (reporttypefk) REFERENCES reporttype(reporttypepk);


--
-- Name: actionrequest sampleunitreffk_fkey; Type: FK CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY actionrequest
    ADD CONSTRAINT sampleunitreffk_fkey FOREIGN KEY (sampleunitreffk) REFERENCES address(sampleunitrefpk);


--
-- Name: templatemapping templatenamefk_fkey; Type: FK CONSTRAINT; Schema: actionexporter; Owner: actionexportersvc
--

ALTER TABLE ONLY templatemapping
    ADD CONSTRAINT templatenamefk_fkey FOREIGN KEY (templatenamefk) REFERENCES template(templatenamepk);


SET search_path = casesvc, pg_catalog;

--
-- Name: caseevent case_fkey; Type: FK CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY caseevent
    ADD CONSTRAINT case_fkey FOREIGN KEY (casefk) REFERENCES "case"(casepk);


--
-- Name: response case_fkey; Type: FK CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY response
    ADD CONSTRAINT case_fkey FOREIGN KEY (casefk) REFERENCES "case"(casepk);


--
-- Name: case casegroup_fkey; Type: FK CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY "case"
    ADD CONSTRAINT casegroup_fkey FOREIGN KEY (casegroupfk) REFERENCES casegroup(casegrouppk);


--
-- Name: caseevent category_fkey; Type: FK CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY caseevent
    ADD CONSTRAINT category_fkey FOREIGN KEY (categoryfk) REFERENCES category(categorypk);


--
-- Name: report reporttypefk_fkey; Type: FK CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT reporttypefk_fkey FOREIGN KEY (reporttypefk) REFERENCES reporttype(reporttypepk);


--
-- Name: case state_fkey; Type: FK CONSTRAINT; Schema: casesvc; Owner: casesvc
--

ALTER TABLE ONLY "case"
    ADD CONSTRAINT state_fkey FOREIGN KEY (statefk) REFERENCES casestate(statepk);


SET search_path = collectionexercise, pg_catalog;

--
-- Name: event event_collexfk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_collexfk_fkey FOREIGN KEY (collexfk) REFERENCES collectionexercise(exercisepk);


--
-- Name: casetypeoverride exercisefk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY casetypeoverride
    ADD CONSTRAINT exercisefk_fkey FOREIGN KEY (exercisefk) REFERENCES collectionexercise(exercisepk);


--
-- Name: sampleunitgroup exercisefk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunitgroup
    ADD CONSTRAINT exercisefk_fkey FOREIGN KEY (exercisefk) REFERENCES collectionexercise(exercisepk);


--
-- Name: report reporttypefk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT reporttypefk_fkey FOREIGN KEY (reporttypefk) REFERENCES reporttype(reporttypepk);


--
-- Name: sampleunit sampleunitgroupfk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunit
    ADD CONSTRAINT sampleunitgroupfk_fkey FOREIGN KEY (sampleunitgroupfk) REFERENCES sampleunitgroup(sampleunitgrouppk);


--
-- Name: casetypedefault sampleunittype_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY casetypedefault
    ADD CONSTRAINT sampleunittype_fkey FOREIGN KEY (sampleunittypefk) REFERENCES sampleunittype(sampleunittypepk);


--
-- Name: casetypeoverride sampleunittypefk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY casetypeoverride
    ADD CONSTRAINT sampleunittypefk_fkey FOREIGN KEY (sampleunittypefk) REFERENCES sampleunittype(sampleunittypepk);


--
-- Name: sampleunit sampleunittypefk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunit
    ADD CONSTRAINT sampleunittypefk_fkey FOREIGN KEY (sampleunittypefk) REFERENCES sampleunittype(sampleunittypepk);


--
-- Name: collectionexercise statefk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY collectionexercise
    ADD CONSTRAINT statefk_fkey FOREIGN KEY (statefk) REFERENCES collectionexercisestate(statepk);


--
-- Name: sampleunitgroup statefk_fkey; Type: FK CONSTRAINT; Schema: collectionexercise; Owner: collectionexercisesvc
--

ALTER TABLE ONLY sampleunitgroup
    ADD CONSTRAINT statefk_fkey FOREIGN KEY (statefk) REFERENCES sampleunitgroupstate(statepk);


SET search_path = partysvc, pg_catalog;

--
-- Name: business_attributes business_attributes_business_id_fkey; Type: FK CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business_attributes
    ADD CONSTRAINT business_attributes_business_id_fkey FOREIGN KEY (business_id) REFERENCES business(party_uuid);


--
-- Name: business_respondent business_respondent_business_id_fkey; Type: FK CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business_respondent
    ADD CONSTRAINT business_respondent_business_id_fkey FOREIGN KEY (business_id) REFERENCES business(party_uuid);


--
-- Name: business_respondent business_respondent_respondent_id_fkey; Type: FK CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY business_respondent
    ADD CONSTRAINT business_respondent_respondent_id_fkey FOREIGN KEY (respondent_id) REFERENCES respondent(id);


--
-- Name: enrolment enrolment_business_id_fkey; Type: FK CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY enrolment
    ADD CONSTRAINT enrolment_business_id_fkey FOREIGN KEY (business_id, respondent_id) REFERENCES business_respondent(business_id, respondent_id);


--
-- Name: pending_enrolment pending_enrolment_respondent_id_fkey; Type: FK CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY pending_enrolment
    ADD CONSTRAINT pending_enrolment_respondent_id_fkey FOREIGN KEY (respondent_id) REFERENCES respondent(id);


--
-- Name: pending_enrolment pending_enrolment_respondent_id_fkey1; Type: FK CONSTRAINT; Schema: partysvc; Owner: postgres
--

ALTER TABLE ONLY pending_enrolment
    ADD CONSTRAINT pending_enrolment_respondent_id_fkey1 FOREIGN KEY (respondent_id) REFERENCES respondent(id);


SET search_path = public, pg_catalog;

--
-- Name: auth_group_permissions auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permiss_permission_id_84c5c92e_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permiss_content_type_id_2f476e4b_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_per_permission_id_1fbb5f2c_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_content_type_id_c4bce8eb_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_content_type_id_c4bce8eb_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthauthorizationcode_scopes e087e784de108b1bb0f263df6a6ee307; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode_scopes
    ADD CONSTRAINT e087e784de108b1bb0f263df6a6ee307 FOREIGN KEY (oauthauthorizationcode_id) REFERENCES tokens_oauthauthorizationcode(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthaccesstoken_scopes toke_oauthaccesstoken_id_9f8ce9f3_fk_tokens_oauthaccesstoken_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken_scopes
    ADD CONSTRAINT toke_oauthaccesstoken_id_9f8ce9f3_fk_tokens_oauthaccesstoken_id FOREIGN KEY (oauthaccesstoken_id) REFERENCES tokens_oauthaccesstoken(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthaccesstoken tokens_oauthac_client_id_0b06e756_fk_credentials_oauthclient_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken
    ADD CONSTRAINT tokens_oauthac_client_id_0b06e756_fk_credentials_oauthclient_id FOREIGN KEY (client_id) REFERENCES credentials_oauthclient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthaccesstoken_scopes tokens_oauthacce_oauthscope_id_75cbc0c6_fk_tokens_oauthscope_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken_scopes
    ADD CONSTRAINT tokens_oauthacce_oauthscope_id_75cbc0c6_fk_tokens_oauthscope_id FOREIGN KEY (oauthscope_id) REFERENCES tokens_oauthscope(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthaccesstoken tokens_oauthaccess_user_id_e5dc07c6_fk_credentials_oauthuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken
    ADD CONSTRAINT tokens_oauthaccess_user_id_e5dc07c6_fk_credentials_oauthuser_id FOREIGN KEY (user_id) REFERENCES credentials_oauthuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthauthorizationcode tokens_oauthau_client_id_a3a1bf9a_fk_credentials_oauthclient_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode
    ADD CONSTRAINT tokens_oauthau_client_id_a3a1bf9a_fk_credentials_oauthclient_id FOREIGN KEY (client_id) REFERENCES credentials_oauthclient(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthauthorizationcode_scopes tokens_oauthauth_oauthscope_id_fa96eff3_fk_tokens_oauthscope_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode_scopes
    ADD CONSTRAINT tokens_oauthauth_oauthscope_id_fa96eff3_fk_tokens_oauthscope_id FOREIGN KEY (oauthscope_id) REFERENCES tokens_oauthscope(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthauthorizationcode tokens_oauthauthor_user_id_4921b0a3_fk_credentials_oauthuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthauthorizationcode
    ADD CONSTRAINT tokens_oauthauthor_user_id_4921b0a3_fk_credentials_oauthuser_id FOREIGN KEY (user_id) REFERENCES credentials_oauthuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tokens_oauthaccesstoken tokens_refresh_token_id_73966741_fk_tokens_oauthrefreshtoken_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tokens_oauthaccesstoken
    ADD CONSTRAINT tokens_refresh_token_id_73966741_fk_tokens_oauthrefreshtoken_id FOREIGN KEY (refresh_token_id) REFERENCES tokens_oauthrefreshtoken(id) DEFERRABLE INITIALLY DEFERRED;


SET search_path = ras_ci, pg_catalog;

--
-- Name: instrument_business instrument_business_business_id_fkey; Type: FK CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY instrument_business
    ADD CONSTRAINT instrument_business_business_id_fkey FOREIGN KEY (business_id) REFERENCES business(id);


--
-- Name: instrument_business instrument_business_instrument_id_fkey; Type: FK CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY instrument_business
    ADD CONSTRAINT instrument_business_instrument_id_fkey FOREIGN KEY (instrument_id) REFERENCES instrument(id);


--
-- Name: instrument_exercise instrument_exercise_exercise_id_fkey; Type: FK CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY instrument_exercise
    ADD CONSTRAINT instrument_exercise_exercise_id_fkey FOREIGN KEY (exercise_id) REFERENCES exercise(id);


--
-- Name: instrument_exercise instrument_exercise_instrument_id_fkey; Type: FK CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY instrument_exercise
    ADD CONSTRAINT instrument_exercise_instrument_id_fkey FOREIGN KEY (instrument_id) REFERENCES instrument(id);


--
-- Name: instrument instrument_survey_id_fkey; Type: FK CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY instrument
    ADD CONSTRAINT instrument_survey_id_fkey FOREIGN KEY (survey_id) REFERENCES survey(id);


--
-- Name: seft_instrument seft_instrument_instrument_id_fkey; Type: FK CONSTRAINT; Schema: ras_ci; Owner: postgres
--

ALTER TABLE ONLY seft_instrument
    ADD CONSTRAINT seft_instrument_instrument_id_fkey FOREIGN KEY (instrument_id) REFERENCES instrument(instrument_id);


SET search_path = sample, pg_catalog;

--
-- Name: report reporttypefk_fkey; Type: FK CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY report
    ADD CONSTRAINT reporttypefk_fkey FOREIGN KEY (reporttypefk) REFERENCES reporttype(reporttypepk);


--
-- Name: sampleunit samplesummary_fkey; Type: FK CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY sampleunit
    ADD CONSTRAINT samplesummary_fkey FOREIGN KEY (samplesummaryfk) REFERENCES samplesummary(samplesummarypk);


--
-- Name: samplesummary statefk_fkey; Type: FK CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY samplesummary
    ADD CONSTRAINT statefk_fkey FOREIGN KEY (statefk) REFERENCES samplesummarystate(statepk);


--
-- Name: sampleunit statefk_fkey; Type: FK CONSTRAINT; Schema: sample; Owner: samplesvc
--

ALTER TABLE ONLY sampleunit
    ADD CONSTRAINT statefk_fkey FOREIGN KEY (statefk) REFERENCES sampleunitstate(statepk);


SET search_path = survey, pg_catalog;

--
-- Name: classifiertype classifiertypeselectorfk_fkey; Type: FK CONSTRAINT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY classifiertype
    ADD CONSTRAINT classifiertypeselectorfk_fkey FOREIGN KEY (classifiertypeselectorfk) REFERENCES classifiertypeselector(classifiertypeselectorpk);


--
-- Name: classifiertypeselector surveyfk_fkey; Type: FK CONSTRAINT; Schema: survey; Owner: postgres
--

ALTER TABLE ONLY classifiertypeselector
    ADD CONSTRAINT surveyfk_fkey FOREIGN KEY (surveyfk) REFERENCES survey(surveypk);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

