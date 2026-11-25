with open("index-v3.html", "r", encoding="utf-8") as f:
    html = f.read()

old_hero_left_bottom = """            <!-- Subtle Key Credentials Bar -->
            <div class="pt-4 flex flex-wrap items-center gap-x-6 gap-y-2 text-xs text-driftwood">
              <span class="inline-flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-oliveSage"></span>
                5+ Years Multi-Site Operations
              </span>
              <span class="inline-flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-cognac"></span>
                Custom CRM &amp; AI Automation Builder
              </span>
            </div>"""

new_hero_left_bottom = """            <!-- Prominent Credential Highlight Boxes (Left: Ops & Systems, Right: B.S. Business Management) -->
            <div class="pt-4 grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-2xl">
              <div class="bg-coconutIvory border border-sandBorder border-l-4 border-l-cognac rounded-lg px-4 py-3.5 shadow-sm flex flex-col justify-center">
                <span class="text-[9.5px] font-semibold tracking-[0.2em] uppercase text-driftwood">
                  Operations &amp; Systems
                </span>
                <span class="text-sm sm:text-[15px] font-semibold text-espresso mt-1 leading-snug">
                  5+ Years Multi-Site Operations
                </span>
                <span class="text-xs font-medium text-roastBrown mt-0.5 leading-snug">
                  Custom CRM &amp; AI Automation Builder
                </span>
              </div>

              <div class="bg-coconutIvory border border-sandBorder border-l-4 border-l-oliveSage rounded-lg px-4 py-3.5 shadow-sm flex flex-col justify-center">
                <span class="text-[9.5px] font-semibold tracking-[0.2em] uppercase text-driftwood">
                  Education
                </span>
                <span class="text-sm sm:text-[15px] font-semibold text-espresso mt-1 leading-snug">
                  B.S. in Business Management
                </span>
                <span class="text-xs font-medium text-roastBrown mt-0.5 leading-snug">
                  Grand Canyon University, Honors College
                </span>
              </div>
            </div>"""

assert old_hero_left_bottom in html, "Could not find old_hero_left_bottom"
html = html.replace(old_hero_left_bottom, new_hero_left_bottom)

old_right_col = """          <!-- Right Column: Headshot Portrait in Arch Editorial Frame -->
          <div class="lg:col-span-5 flex justify-center lg:justify-end">
            <div class="relative w-full max-w-[350px] sm:max-w-[390px]">
              <figure class="arch-frame overflow-hidden border border-sandBorder bg-toastedOat aspect-[4/4.85] relative shadow-[0_20px_50px_-15px_rgba(36,25,19,0.18)] flex flex-col justify-between">
                <img
                  id="dakota-headshot"
                  src="https://drive.google.com/thumbnail?id=1AGCEtbeZPKK2KxLK1yBt8Ynokyb8-von&sz=w1200"
                  data-fallback-lh3="https://lh3.googleusercontent.com/d/1AGCEtbeZPKK2KxLK1yBt8Ynokyb8-von=w1200"
                  data-fallback-local="SHEF5052.jpg"
                  data-fallback-label="Dakota+Taylor"
                  alt="Dakota Taylor portrait in warm neutral tones"
                  class="w-full h-full object-cover flex-1"
                  style="object-fit: cover; object-position: center 20%;"
                  onerror="handleDriveImageError(this)"
                />
                <figcaption class="bg-coconutIvory/95 backdrop-blur-sm border-t border-sandBorder px-4 py-2.5 flex items-center justify-between gap-2 text-[10px] font-semibold tracking-[0.18em] uppercase text-roastBrown shrink-0">
                  <span>Dakota Taylor</span>
                  <a
                    href="https://drive.google.com/file/d/1AGCEtbeZPKK2KxLK1yBt8Ynokyb8-von/view?usp=sharing"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-cognac hover:text-espresso underline decoration-sandBorder underline-offset-4 transition-colors"
                  >
                    Full Photo &#8599;
                  </a>
                </figcaption>
              </figure>

              <!-- Floating Badge -->
              <div class="absolute -bottom-4 left-4 sm:-left-6 bg-coconutIvory/95 backdrop-blur-md border border-sandBorder border-l-4 border-l-oliveSage px-5 py-3.5 shadow-lg rounded-sm">
                <span class="block text-[9px] font-semibold tracking-[0.22em] uppercase text-driftwood">Based In</span>
                <span class="block text-sm sm:text-base font-medium text-espresso mt-0.5">Phoenix, Arizona</span>
              </div>
            </div>
          </div>"""

new_right_col = """          <!-- Right Column: Headshot Portrait in Arch Editorial Frame + Summary Box Below -->
          <div class="lg:col-span-5 flex flex-col items-center lg:items-end space-y-5">
            <div class="relative w-full max-w-[350px] sm:max-w-[390px]">
              <figure class="arch-frame overflow-hidden border border-sandBorder bg-toastedOat aspect-[4/4.85] relative shadow-[0_20px_50px_-15px_rgba(36,25,19,0.18)] flex flex-col justify-between">
                <img
                  id="dakota-headshot"
                  src="https://drive.google.com/thumbnail?id=1AGCEtbeZPKK2KxLK1yBt8Ynokyb8-von&sz=w1200"
                  data-fallback-lh3="https://lh3.googleusercontent.com/d/1AGCEtbeZPKK2KxLK1yBt8Ynokyb8-von=w1200"
                  data-fallback-local="SHEF5052.jpg"
                  data-fallback-label="Dakota+Taylor"
                  alt="Dakota Taylor portrait in warm neutral tones"
                  class="w-full h-full object-cover flex-1"
                  style="object-fit: cover; object-position: center 20%;"
                  onerror="handleDriveImageError(this)"
                />
                <figcaption class="bg-coconutIvory/95 backdrop-blur-sm border-t border-sandBorder px-4 py-2.5 flex items-center justify-between gap-2 text-[10px] font-semibold tracking-[0.18em] uppercase text-roastBrown shrink-0">
                  <span>Dakota Taylor</span>
                  <a
                    href="https://drive.google.com/file/d/1AGCEtbeZPKK2KxLK1yBt8Ynokyb8-von/view?usp=sharing"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-cognac hover:text-espresso underline decoration-sandBorder underline-offset-4 transition-colors"
                  >
                    Full Photo &#8599;
                  </a>
                </figcaption>
              </figure>

              <!-- Floating Badge -->
              <div class="absolute -bottom-4 left-4 sm:-left-6 bg-coconutIvory/95 backdrop-blur-md border border-sandBorder border-l-4 border-l-oliveSage px-5 py-3.5 shadow-lg rounded-sm">
                <span class="block text-[9px] font-semibold tracking-[0.22em] uppercase text-driftwood">Based In</span>
                <span class="block text-sm sm:text-base font-medium text-espresso mt-0.5">Phoenix, Arizona</span>
              </div>
            </div>

            <!-- Credential Summary Box Underneath Photo (Editorial Divider Style) -->
            <div class="w-full max-w-[350px] sm:max-w-[390px] pt-3 bg-coconutIvory/90 border border-sandBorder rounded-lg px-5 py-4 shadow-sm">
              <div class="grid grid-cols-3 divide-x divide-sandBorder text-left">
                <div class="pr-3">
                  <span class="block font-serif text-base sm:text-lg font-normal text-cognac leading-tight">5+ Years</span>
                  <span class="block text-[9px] font-semibold tracking-[0.14em] uppercase text-roastBrown mt-1 leading-snug">
                    in Business Operations
                  </span>
                </div>
                <div class="px-3">
                  <span class="block font-serif text-base sm:text-lg font-normal text-espresso leading-tight">Custom CRM</span>
                  <span class="block text-[9px] font-semibold tracking-[0.14em] uppercase text-roastBrown mt-1 leading-snug">
                    &amp; AI Automation Builder
                  </span>
                </div>
                <div class="pl-3">
                  <span class="block font-serif text-base sm:text-lg font-normal text-oliveSage leading-tight">B.S.</span>
                  <span class="block text-[9px] font-semibold tracking-[0.14em] uppercase text-roastBrown mt-1 leading-snug">
                    in Business Management
                  </span>
                </div>
              </div>
            </div>
          </div>"""

assert old_right_col in html, "Could not find old_right_col"
html = html.replace(old_right_col, new_right_col)

with open("index-v4.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully wrote index-v4.html")