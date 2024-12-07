export interface GetMessageDto {
    id: number;
    text?: string;
    file_id?: number;
    answer_text?: string;
    answer_file_id?: number;
    public: boolean;
}
