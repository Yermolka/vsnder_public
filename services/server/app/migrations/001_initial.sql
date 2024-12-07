CREATE TABLE "user" (
	"id" SERIAL PRIMARY KEY,
	"username" VARCHAR(64) NOT NULL,
	"password_hash" VARCHAR NOT NULL,
	"original_password" VARCHAR NOT NULL,
	"first_name" VARCHAR(64) NOT NULL,
	"last_name" VARCHAR(64) NOT NULL,
	"age" int2 NULL,
	"orientation" VARCHAR NULL,
	"interests" VARCHAR NULL,
	"vsn_interests" VARCHAR NULL,
	"places_to_visit" VARCHAR NULL,
	"study_places" VARCHAR NULL,
	"music" VARCHAR NULL,
	"favorite_movies" VARCHAR NULL,
	"religion" VARCHAR NULL,
	"status" VARCHAR NULL,
	"future_plans" VARCHAR NULL,
	"family_opinion" VARCHAR NULL,
	"favorite_programming_language" VARCHAR NULL,
	"lizards_or_russians" bool DEFAULT true NULL,
	"top_3_people" VARCHAR NULL,
	"smoking" VARCHAR NULL,
	"drinking" VARCHAR NULL,
	"created" TIMESTAMP DEFAULT NOW() NOT NULL,
	"modified" TIMESTAMP DEFAULT NOW() NOT NULL,
	"year_of_study" INT DEFAULT 1 NOT NULL,
	"has_avatar" BOOL DEFAULT FALSE NOT NULL,
	"birth_stamp" TIMESTAMP NULL,
	"birth_city" VARCHAR(128) NULL,
	CONSTRAINT "user_year_of_study_check" CHECK ((("year_of_study" > 0) AND ("year_of_study" < 5)))
);
CREATE UNIQUE INDEX "user_login_index" ON "user" USING btree (username);

CREATE TABLE "message" (
	"id" SERIAL PRIMARY KEY,
	"receiver_id" INT NOT NULL REFERENCES "user" ON DELETE CASCADE,
	"text" VARCHAR NULL,
	"picture" BYTEA NULL,
	"media_type" VARCHAR NULL
);
CREATE INDEX "message_id_idx" ON "message" USING btree ("id");
CREATE INDEX "message_receiver_id_idx" ON "message" USING btree ("receiver_id");

CREATE TABLE "file" (
	"id" SERIAL PRIMARY KEY,
	"user_id" INT NOT NULL REFERENCES "user" ON DELETE CASCADE,
	"media_type" VARCHAR NOT NULL,
	"data" BYTEA NULL
);
CREATE UNIQUE INDEX "per_user_picture_unique" ON "file" USING btree ("user_id");

CREATE TABLE "analytic_logs" (
	"id" SERIAL PRIMARY KEY,
	"user_id" INT NOT NULL REFERENCES "user" ON DELETE CASCADE,
	"data" VARCHAR NOT NULL,
	"time" TIMESTAMP DEFAULT NOW() NOT NULL
);
CREATE INDEX "analytic_logs_data_idx" ON "analytic_logs" USING btree ("data");
CREATE INDEX "analytic_logs_user_id_idx" ON "analytic_logs" USING btree ("user_id");
