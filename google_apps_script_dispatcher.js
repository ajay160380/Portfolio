/**
 * =========================================================================
 * AJAY VISHWAKARMA PORTFOLIO - ULTRA-PREMIUM LEAD DISPATCHER
 * =========================================================================
 * 
 * Instructions to deploy in 2 minutes (100% Free forever):
 * 1. Open https://script.google.com/ in your browser.
 * 2. Click "New Project" (+ New project).
 * 3. Delete any default code inside Code.gs, and paste this entire code.
 * 4. Click "Deploy" (top right blue button) > "New deployment".
 * 5. Under "Select type" (gear icon), select "Web app".
 * 6. Set Description: "Portfolio Lead Webhook"
 *    - Execute as: "Me (your email)"
 *    - Who has access: "Anyone" (important for web form submissions)
 * 7. Click "Deploy" and Authorize access with your Google account.
 * 8. Copy the "Web app URL" (e.g. https://script.google.com/macros/s/AKfycb.../exec).
 * 9. Paste this URL into your website's config (or set window.PORTFOLIO_EMAIL_ENDPOINT = "URL").
 * =========================================================================
 */

function doGet() {
  return ContentService.createTextOutput("🟢 Ajay Vishwakarma Portfolio Lead Webhook is ACTIVE.")
    .setMimeType(ContentService.MimeType.TEXT);
}

function doPost(e) {
  try {
    var raw = e.postData ? e.postData.contents : "";
    var data = {};
    if (raw) {
      try {
        data = JSON.parse(raw);
      } catch (err) {
        data = e.parameter || {};
      }
    } else {
      data = e.parameter || {};
    }

    var clientName = (data.name || data["👤 CLIENT NAME"] || "Portfolio Visitor").toString().trim();
    var clientEmail = (data.email || data["📧 CLIENT EMAIL"] || "").toString().trim();
    var clientMessage = (data.message || data["💼 SELECTED SERVICES & SCOPE"] || "Portfolio Collaboration Inquiry").toString().trim();
    var origin = (data.origin || data["🌐 SUBMITTED FROM"] || "ajay-portfolio-r176.onrender.com").toString().trim();
    var timestamp = (data.timestamp || data["⏰ RECEIVED AT (IST)"] || (new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata", dateStyle: "full", timeStyle: "medium" }) + " IST")).toString();

    // Compute initials for the avatar
    var initials = "VIP";
    if (clientName) {
      var parts = clientName.split(/\s+/);
      if (parts.length >= 2) {
        initials = (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
      } else if (parts.length === 1 && parts[0].length > 0) {
        initials = parts[0].slice(0, 2).toUpperCase();
      }
    }

    // Build badge pills
    var badgesHtml = "";
    var scopeParts = clientMessage.split(/[,—]/);
    for (var i = 0; i < scopeParts.length; i++) {
      var tag = scopeParts[i].trim();
      if (tag.length > 0) {
        badgesHtml += '<span style="display: inline-block; background-color: #1a2337; border: 1px solid #2a3958; color: #e2e8f0; font-size: 13px; font-weight: 500; padding: 7px 14px; border-radius: 8px; margin: 0 6px 6px 0;">' + tag + '</span>';
      }
    }
    if (!badgesHtml) {
      badgesHtml = '<span style="display: inline-block; background-color: #1a2337; border: 1px solid #2a3958; color: #e2e8f0; font-size: 13px; font-weight: 500; padding: 7px 14px; border-radius: 8px;">💼 Portfolio Collaboration</span>';
    }

    var recipientEmail = "ajaykumar160380@gmail.com";
    var firstScope = clientMessage.split(/[,—]/)[0] ? clientMessage.split(/[,—]/)[0].trim() : "Project Inquiry";
    var emailSubject = "✨ [VIP Lead] " + clientName + " — " + firstScope;

    var htmlBody = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">' +
      '<html xmlns="http://www.w3.org/1999/xhtml">' +
      '<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>' + emailSubject + '</title></head>' +
      '<body style="margin: 0; padding: 30px 10px; background-color: #07090e; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">' +
      '<table border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;">' +
        '<tr><td align="center">' +
          '<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: #0d121f; border-radius: 18px; border: 1px solid #1e293b; overflow: hidden; box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);">' +
            '<tr><td height="4" style="background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%); font-size: 0; line-height: 0;">&nbsp;</td></tr>' +
            '<tr>' +
              '<td style="padding: 28px 32px 20px 32px; border-bottom: 1px solid #182234;">' +
                '<table border="0" cellpadding="0" cellspacing="0" width="100%">' +
                  '<tr>' +
                    '<td valign="middle" width="46">' +
                      '<div style="width: 38px; height: 38px; border-radius: 10px; background: linear-gradient(135deg, #0284c7, #6366f1); text-align: center; line-height: 38px; font-weight: 800; font-size: 14px; color: #ffffff; letter-spacing: 0.5px;">AV</div>' +
                    '</td>' +
                    '<td valign="middle">' +
                      '<div style="font-size: 13px; font-weight: 700; letter-spacing: 1.2px; color: #f8fafc; text-transform: uppercase;">AJAY VISHWAKARMA</div>' +
                      '<div style="font-size: 11px; color: #94a3b8; letter-spacing: 0.3px; margin-top: 2px;">Senior AI & Full-Stack Engineer • Portfolio Dispatch</div>' +
                    '</td>' +
                    '<td valign="middle" align="right">' +
                      '<span style="display: inline-block; background-color: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); color: #34d399; font-size: 11px; font-weight: 700; padding: 5px 12px; border-radius: 20px; letter-spacing: 0.5px; text-transform: uppercase;">🟢 PRIORITY LEAD</span>' +
                    '</td>' +
                  '</tr>' +
                '</table>' +
              '</td>' +
            '</tr>' +
            '<tr>' +
              '<td style="padding: 32px 32px 24px 32px;">' +
                '<div style="font-size: 22px; font-weight: 700; color: #ffffff; margin-bottom: 6px; letter-spacing: -0.3px;">New Project Collaboration Request</div>' +
                '<div style="font-size: 14px; color: #94a3b8; line-height: 1.5; margin-bottom: 24px;">A new client inquiry was submitted directly via your interactive 3D WebGL portfolio.</div>' +
                '<table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #141b2c; border: 1px solid #1f293d; border-radius: 14px; margin-bottom: 24px;">' +
                  '<tr><td style="padding: 18px 20px;">' +
                    '<table border="0" cellpadding="0" cellspacing="0" width="100%">' +
                      '<tr>' +
                        '<td width="56" valign="middle">' +
                          '<div style="width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg, #3b82f6, #8b5cf6); text-align: center; line-height: 48px; font-size: 18px; font-weight: 700; color: #ffffff;">' + initials + '</div>' +
                        '</td>' +
                        '<td valign="middle" style="padding-left: 12px;">' +
                          '<div style="font-size: 17px; font-weight: 700; color: #ffffff; margin-bottom: 3px;">' + clientName + '</div>' +
                          '<div><a href="mailto:' + clientEmail + '" style="font-size: 13px; color: #38bdf8; text-decoration: none; font-family: ui-monospace, Menlo, Consolas, monospace;">' + clientEmail + '</a></div>' +
                        '</td>' +
                      '</tr>' +
                    '</table>' +
                  '</td></tr>' +
                '</table>' +
                '<div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #94a3b8; margin-bottom: 12px;">🎯 SELECTED FOCUS & SERVICES</div>' +
                '<div style="margin-bottom: 24px;">' + badgesHtml + '</div>' +
                '<div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #94a3b8; margin-bottom: 12px;">📝 PROJECT SCOPE & INQUIRIES</div>' +
                '<div style="background-color: #141b2c; border-left: 3px solid #38bdf8; border-radius: 0 10px 10px 0; padding: 16px 20px; font-size: 14px; line-height: 1.6; color: #cbd5e1; margin-bottom: 28px;">' + clientMessage + '</div>' +
                '<table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 28px;">' +
                  '<tr><td align="center">' +
                    '<a href="mailto:' + clientEmail + '?subject=Re:%20Collaboration%20Inquiry%20-%20Ajay%20Vishwakarma" target="_blank" style="display: block; width: 100%; box-sizing: border-box; background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%); color: #ffffff; text-decoration: none; font-size: 15px; font-weight: 700; text-align: center; padding: 16px 24px; border-radius: 12px; letter-spacing: 0.3px; box-shadow: 0 8px 20px rgba(37, 99, 235, 0.45);">' +
                      '✉️ Reply Directly to ' + clientName +
                    '</a>' +
                  '</td></tr>' +
                '</table>' +
                '<table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-top: 1px solid #1a2333; padding-top: 18px;">' +
                  '<tr>' +
                    '<td width="50%" valign="top">' +
                      '<div style="font-size: 11px; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px;">RECEIVED AT (IST)</div>' +
                      '<div style="font-size: 13px; color: #cbd5e1; font-weight: 500; margin-top: 3px;">' + timestamp + '</div>' +
                    '</td>' +
                    '<td width="50%" valign="top">' +
                      '<div style="font-size: 11px; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px;">SUBMISSION SOURCE</div>' +
                      '<div style="font-size: 13px; color: #cbd5e1; font-weight: 500; margin-top: 3px;">' + origin + '</div>' +
                    '</td>' +
                  '</tr>' +
                '</table>' +
              '</td>' +
            '</tr>' +
            '<tr>' +
              '<td style="padding: 22px 32px; background-color: #090d16; border-top: 1px solid #141b27; text-align: center;">' +
                '<div style="font-size: 12px; color: #64748b; line-height: 1.6;">' +
                  'Sent securely from <strong style="color: #94a3b8;">Ajay Vishwakarma\'s Interactive Portfolio</strong><br />' +
                  'Direct VIP Dispatch • End-to-End Privacy Guaranteed' +
                '</div>' +
                '<div style="margin-top: 10px; font-size: 11px;">' +
                  '<a href="https://ajay-portfolio-r176.onrender.com/" style="color: #94a3b8; text-decoration: none; margin: 0 8px;">Portfolio</a> • ' +
                  '<a href="https://github.com/ajay160380" style="color: #94a3b8; text-decoration: none; margin: 0 8px;">GitHub</a> • ' +
                  '<a href="https://linkedin.com/in/ajay-vishwakarma-ai" style="color: #94a3b8; text-decoration: none; margin: 0 8px;">LinkedIn</a>' +
                '</div>' +
              '</td>' +
            '</tr>' +
          '</table>' +
        '</td></tr>' +
      '</table>' +
      '</body></html>';

    MailApp.sendEmail({
      to: recipientEmail,
      replyTo: clientEmail || recipientEmail,
      subject: emailSubject,
      name: "Ajay Portfolio Leads",
      htmlBody: htmlBody
    });

    return ContentService.createTextOutput(JSON.stringify({ status: "success", message: "Email sent" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

