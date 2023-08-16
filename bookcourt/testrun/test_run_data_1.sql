insert into common_tenant ( name, sign_up_terms_and_conditions, booking_terms_and_conditions, is_active) values ('Cloverbridge Technologies Pvt Ltd', 'I agree to the sign up terms and conditions', 'I agree to the booking terms and conditions', 't');



insert into auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) values ('pbkdf2_sha256$260000$Ez0XlPiH6XCeN9cX8iJihB$D78XA9fHr2F3/yGNp8O/Mjb4V6sSeOcuGNQ+b8zwp0s=', 'f', 'rugved', 'rugved', '', 'rugved@gmail.com', 'f', 't', now()),
('pbkdf2_sha256$260000$Ez0XlPiH6XCeN9cX8iJihB$D78XA9fHr2F3/yGNp8O/Mjb4V6sSeOcuGNQ+b8zwp0s=', 'f', 'Alpha Game Club', 'alpha', '', 'alphagameclub@gmail.com', 'f', 't', now());



insert into common_customer (user_ptr_id, tenant_id) values ((select id from auth_user where username='rugved'), (select id from common_tenant where name='Cloverbridge Technologies Pvt Ltd'));


insert into common_locationcity (tenant_id, city, is_active) values ((select id from common_tenant where id=1), 'Chennai', 't');


insert into common_locationarea (tenant_id, area, is_active) values
((select id from common_tenant where id=1), 'Arumbakkam', 't'),
((select id from common_tenant where id=1), 'Guindy', 't');


insert into common_organization(user_ptr_id, organization_name, alt_number, description, is_terms_and_conditions_agreed, status, tenant_id ) values ((select id from auth_user where username='Alpha Game Club'), 'Alpha Game Club', '5876543210', 'we have best courts', 'f', '2', (select id from common_tenant where name='Cloverbridge Technologies Pvt Ltd'));


insert into common_gametype (name, is_active) values('Badminton', 't'),('Cricket', 't'), ('Table Tennis', 't');


insert into common_organizationlocation (address_line_1, address_line_2, area, city, state, pincode, contact_number, join_date, created_date, created_time, organization_id, is_active) values
('No.10 2nd avenue', 'jai nagar', 'Arumbakkam', 'Chennai', 'Tamilnadu', '600106', '5432167890', now(), now(), now(),(select id from auth_user where id = 3), 't'),
('No.10 15th cross street', 'AK colony', 'Guindy', 'Chennai', 'Tamilnadu', '600053', '4321567890', now(), now(), now(),(select id from auth_user where id = 3), 't');


insert into common_organizationlocationworkingdays(organization_location_id, is_monday_workingday, is_tuesday_workingday, is_wednesday_workingday, is_thursday_workingday, is_friday_workingday, is_saturday_workingday, is_sunday_workingday) values
((select id from common_organizationlocation where id = 2), 't', 't', 't', 't', 't', 't', 't'),
((select id from common_organizationlocation where id = 3), 't', 't', 't', 't', 't', 't', 't');


insert into common_OrganizationlocationAmenities (organization_location_id, is_parking, is_restrooms, is_changerooms, is_powerbackup, is_beverages_facility, is_coaching_facilities, description) values
((select id from common_organizationlocation where id = 2), 't', 't', 't', 't', 'f', 't', 'We provide best in-class facility to our customers in Arumbakkam'),
((select id from common_organizationlocation where id = 3), 't', 't', 't', 'f', 'f', 'f', 'We provide best in-class facility to our customers in Guindy');


insert into common_OrganizationLocationGameType (pricing, is_active, description, price_calculate_timing, organization_location_id, game_type_id) values
('500', 't', 'best location for badminton in arumbakkam', '0', (select id from common_organizationlocation where id = 2), (select id from common_gametype where id=1));
