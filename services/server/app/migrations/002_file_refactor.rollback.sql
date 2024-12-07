ALTER TABLE "user"
DROP COLUMN "file_id";

ALTER TABLE "user"
ADD COLUMN "has_avatar" BOOL DEFAULT FALSE;

ALTER TABLE "message"
DROP COLUMN "file_id";

ALTER TABLE "message"
ADD COLUMN "media_type" VARCHAR;

ALTER TABLE "message"
ADD COLUMN "picture" BYTEA;

ALTER TABLE "file"
CREATE UNIQUE INDEX "per_user_picture_unique" on "file" USING btree ("user_id");
