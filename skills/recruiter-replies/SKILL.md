---
name: recruiter-replies
description: Monthly recruiter reply & archive workflow for Gmail (wallace.espindola@gmail.com). Use when asked to "answer my recruiter emails", "run the recruiter replies", or "clean recruiter inbox this month". Finds recruiter emails, replies in EN/FR/PT with the not-available template, archives every answered thread.
---

# SKILL: Monthly recruiter reply & archive (Gmail — wallace.espindola@gmail.com)

## Trigger
"Answer my recruiter emails", "run the recruiter replies", "clean recruiter inbox this month".

## Golden rule
EVERY recruiter email that gets an answer MUST be archived right after the answer is sent.
Nothing answered stays in the inbox. Archive only — never delete, never empty trash.

## Step 1 — Find candidates
Search: in:inbox after:YYYY/MM/01
Plus keyword pass: in:inbox after:YYYY/MM/01 (opportunity OR opportunité OR oportunidade OR
recruiter OR recruitment OR recrutement OR recrutamento OR vacancy OR vacature OR vaga OR
"your profile" OR "votre profil" OR consultant OR headhunter OR staffing)
Keep only real person-to-person recruiter mails. EXCLUDE automated job boards
(Indeed, LinkedIn alerts, Eventbrite), newsletters, invoices, timesheets.

## Step 2 — Check what was already answered
Search: in:sent after:YYYY/MM/01 → any thread already containing a reply from me is skipped.
If the SAME recruiter sent several mails this month: reply only to the most recent one;
the others count as "already responded similarly" → archive them without replying.

## Step 3 — Determine language & name
Language of the recruiter's email body: EN → English, FR → French, PT → Portuguese,
anything else (NL, DE, IT…) → English.
Recruiter first name = from signature / sender name → goes into "Hello <name>,"

## Step 4 — Compose the reply
Open thread → Reply → click in body → cmd+Up → shift+Down ×3 → shift+End
(selects the empty line + the auto-signature "--/Wallace Espindola/GSM: +32 467 603 248")
→ type the template over it. This preserves the quoted original message.
Formatting: blank line between every paragraph; signature block lines consecutive (no blank lines).

### English
Hello <name>,

Thank you for reaching out.

The opportunity sounds interesting. However, I'm not available at the moment, as I'm currently committed to a freelance contract for the next few months.

Please feel free to keep me informed about new opportunities and open positions. I'm always happy to take a look and stay up to date with roles that may be a good fit.

Let's keep in touch for future opportunities, and I'd be happy to connect on LinkedIn as well.

Best regards,

Wallace Espindola
Solution Architect | Java & Python Sr. Developer
LinkedIn: https://www.linkedin.com/in/wallaceespindola
GitHub: https://github.com/wallaceespindola
Mobile: +32 467 603 248

### Français
Bonjour <name>,

Merci de m'avoir contacté.

L'opportunité semble intéressante. Cependant, je ne suis pas disponible pour le moment, car je suis actuellement engagé sur une mission freelance pour les prochains mois.

N'hésitez pas à continuer à me tenir informé des nouvelles opportunités et des postes ouverts. Je prends toujours le temps de les consulter afin de rester au courant des opportunités qui pourraient correspondre à mon profil.

Restons en contact pour de futures opportunités. Ce sera également avec plaisir que je vous ajouterai à mon réseau LinkedIn.

Bien cordialement,

Wallace Espindola
Solution Architect | Développeur Sr. Java & Python
LinkedIn : https://www.linkedin.com/in/wallaceespindola
GitHub : https://github.com/wallaceespindola
GSM : +32 467 603 248

### Português (Brasil)
Olá <name>,

Obrigado por entrar em contato.

A oportunidade parece interessante. No entanto, não estou disponível no momento, pois atualmente estou comprometido com um contrato freelance pelos próximos meses.

Por favor, fique à vontade para continuar me enviando novas oportunidades e vagas em aberto. Sempre procuro dar uma olhada para me manter atualizado sobre posições que possam ser interessantes para o meu perfil.

Vamos manter contato para futuras oportunidades. Também ficarei feliz em nos conectarmos pelo LinkedIn.

Atenciosamente,

Wallace Espindola
Solution Architect | Desenvolvedor Sr. Java & Python
LinkedIn: https://www.linkedin.com/in/wallaceespindola
GitHub: https://github.com/wallaceespindola
Celular: +32 467 603 248

## Step 5 — ARCHIVE ALL ANSWERED (mandatory)
After answering, archive all answered emails.
Search: in:inbox after:YYYY/MM/01 from:(name1 OR name2 OR …)
→ select-all checkbox → Archive button (box with down arrow, 2nd in toolbar).
Also archive the same-recruiter duplicates that were intentionally not answered.

## Step 6 — Verify
Re-run the same in:inbox search → must return "No messages matched".
Re-run it without in:inbox → the threads must still exist (archived, not deleted).

## Step 7 — Report
List: who was answered, in which language, and what was archived without reply.

## Rules
- Always show me the candidate list and get my confirmation before sending.
- Never reply twice to the same recruiter in the same month.
- Archive, never delete.
