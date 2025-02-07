<?php
class PHP_Email_Form {
    public $to;
    public $from_name;
    public $from_email;
    public $subject;
    public $smtp = array();
    public $ajax = false;
    private $messages = array();

    public function add_message($content, $label, $priority = 1) {
        $this->messages[] = "{$label}: {$content}";
    }

    public function send() {
        $headers = "From: " . $this->from_name . " <" . $this->from_email . ">\r\n";
        $headers .= "Reply-To: " . $this->from_email . "\r\n";
        $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
        
        $message_body = implode("\n", $this->messages);
        
        if (mail($this->to, $this->subject, $message_body, $headers)) {
            return 'Message sent successfully!';
        } else {
            return 'Message sending failed!';
        }
    }
}
?>
