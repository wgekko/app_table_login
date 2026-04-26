import streamlit as st

def render_animation():

    st.markdown("""
    <style>

    /* ===== BASE ===== */
    body {
        background: hsl(153,90%,10%);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* ===== MICROCHIP ===== */
    .microchip {
        width: 180px;
        margin: 30px auto;
        display: block;
        color: hsl(153,90%,70%);
    }

    /* ===== ANIM BASE ===== */
    .microchip__center,
    .microchip__dot,
    .microchip__line,
    .microchip__lines,
    .microchip__spark,
    .microchip__wave {
        animation-duration: 5s;
        animation-timing-function: cubic-bezier(0.65,0,0.35,1);
        animation-iteration-count: infinite;
    }

    /* ===== COLORS ===== */
    .microchip__core,
    .microchip__dot {
        fill: hsl(153,90%,30%);
    }

    .microchip__line {
        stroke: hsl(153,90%,30%);
    }

    .microchip__spark,
    .microchip__wave {
        stroke: hsl(153,90%,70%);
    }
    .microchip__wave {
        transform-origin: 25px 25px;
        transform-box: fill-box;
    }            

    /* ===== CENTER ===== */
    .microchip__center {
        animation-name: center-scale;
        transform-origin: 25px 25px;
    }

    /* ===== DOTS ===== */
    .microchip__dot--1 { animation: dot1 5s infinite; transform-origin:3px 38px;}
    .microchip__dot--2 { animation: dot2 5s infinite; transform-origin:3px 54px;}
    .microchip__dot--3 { animation: dot3 5s infinite; transform-origin:3px 70px;}
    .microchip__dot--4 { animation: dot4 5s infinite; transform-origin:3px 3px;}
    .microchip__dot--5 { animation: dot5 5s infinite; transform-origin:20px 3px;}
    .microchip__dot--6 { animation: dot6 5s infinite; transform-origin:3px 30px;}
    .microchip__dot--7 { animation: dot7 5s infinite; transform-origin:37px 3px;}
    .microchip__dot--8 { animation: dot8 5s infinite; transform-origin:54px 3px;}
    .microchip__dot--9 { animation: dot9 5s infinite; transform-origin:71px 3px;}

    /* ===== LINES ===== */
    .microchip__line--1 { animation-name: line1; }
    .microchip__line--2 { animation-name: line2; }
    .microchip__line--3 { animation-name: line3; }
    .microchip__line--4 { animation-name: line4; }
    .microchip__line--5 { animation-name: line5; }
    .microchip__line--6 { animation-name: line6; }
    .microchip__line--7 { animation-name: line7; }
    .microchip__line--8 { animation-name: line8; }
    .microchip__line--9 { animation-name: line9; }

    /* ===== SPARKS ===== */
    .microchip__spark--1 { animation-name: spark1; }
    .microchip__spark--2 { animation-name: spark2; }
    .microchip__spark--3 { animation-name: spark3; }
    .microchip__spark--4 { animation-name: spark4; }
    .microchip__spark--5 { animation-name: spark5; }
    .microchip__spark--6 { animation-name: spark6; }
    .microchip__spark--7 { animation-name: spark7; }
    .microchip__spark--8 { animation-name: spark8; }
    .microchip__spark--9 { animation-name: spark9; }

    /* ===== WAVES ===== */
    .microchip__wave--1 { animation: wave1 5s linear infinite; }
    .microchip__wave--2 { animation: wave2 5s linear infinite; }

    /* ===== KEYFRAMES ===== */
    @keyframes center-scale {
        0%,100% {transform:scale(0);}
        12.5%,75% {transform:scale(1);}
    }
                
    /* ===== SINCRONIZACIÓN ===== */

    /* Core primero */
    .microchip__center {
        animation-delay: 0s;
    }

    /* Waves después */
    .microchip__wave--1 { animation-delay: 0.4s; }
    .microchip__wave--2 { animation-delay: 0.6s; }

    /* Líneas */
    .microchip__line { 
        animation-delay: 0.8s;
    }

    /* Sparks */
    .microchip__spark { 
        animation-delay: 1.2s;
    }

    /* Dots al final */
    .microchip__dot { 
        animation-delay: 1.6s;
    }

    /* ===== GLOW NEÓN ===== */

    /* Core glow fuerte */
    .microchip__core {
        filter: drop-shadow(0 0 6px hsl(153,90%,50%))
                drop-shadow(0 0 12px hsl(153,90%,40%))
                drop-shadow(0 0 20px hsl(153,90%,30%));
    }

    /* Líneas glow medio */
    .microchip__line {
        filter: drop-shadow(0 0 4px hsl(153,90%,50%));
    }

    /* Sparks glow intenso */
    .microchip__spark {
        filter: drop-shadow(0 0 6px hsl(153,90%,60%))
                drop-shadow(0 0 10px hsl(153,90%,50%));
    }

    /* Dots glow suave */
    .microchip__dot {
        filter: drop-shadow(0 0 3px hsl(153,90%,60%));
    }

    /* Waves glow difuso */
    .microchip__wave {
        filter: drop-shadow(0 0 8px hsl(153,90%,60%));
    }            
                

    /* DOTS (simplificados pero funcionales) */
    @keyframes dot1 {0%,80%,100%{transform:scale(0);}30%,70%{transform:scale(1);}}
    @keyframes dot2 {0%,85%,100%{transform:scale(0);}25%,75%{transform:scale(1);}}
    @keyframes dot3 {0%,80%,100%{transform:scale(0);}30%,70%{transform:scale(1);}}
    @keyframes dot4 {0%,80%,100%{transform:scale(0);}30%,70%{transform:scale(1);}}
    @keyframes dot5 {0%,85%,100%{transform:scale(0);}25%,75%{transform:scale(1);}}
    @keyframes dot6 {0%,85%,100%{transform:scale(0);}27%,72%{transform:scale(1);}}
    @keyframes dot7 {0%,80%,100%{transform:scale(0);}30%,70%{transform:scale(1);}}
    @keyframes dot8 {0%,85%,100%{transform:scale(0);}25%,75%{transform:scale(1);}}
    @keyframes dot9 {0%,80%,100%{transform:scale(0);}30%,70%{transform:scale(1);}}

    /* LINES */
    @keyframes line1 {0%,100%{stroke-dashoffset:59;}25%,70%{stroke-dashoffset:17;}}
    @keyframes line2 {0%,100%{stroke-dashoffset:42;}25%,70%{stroke-dashoffset:0;}}
    @keyframes line3 {0%,100%{stroke-dashoffset:59;}25%,70%{stroke-dashoffset:17;}}
    @keyframes line4 {0%,100%{stroke-dashoffset:78;}25%,70%{stroke-dashoffset:18;}}
    @keyframes line5 {0%,100%{stroke-dashoffset:60;}25%,70%{stroke-dashoffset:0;}}
    @keyframes line6 {0%,100%{stroke-dashoffset:91;}25%,70%{stroke-dashoffset:31;}}
    @keyframes line7 {0%,100%{stroke-dashoffset:60;}25%,70%{stroke-dashoffset:17;}}
    @keyframes line8 {0%,100%{stroke-dashoffset:43;}25%,70%{stroke-dashoffset:0;}}
    @keyframes line9 {0%,100%{stroke-dashoffset:60;}25%,70%{stroke-dashoffset:17;}}

    /* SPARKS */
    @keyframes spark1 {0%{stroke-dashoffset:59;}50%{stroke-dashoffset:-25;}100%{stroke-dashoffset:-109;}}
    @keyframes spark2 {0%{stroke-dashoffset:42;}50%{stroke-dashoffset:-42;}100%{stroke-dashoffset:-126;}}
    @keyframes spark3 {0%{stroke-dashoffset:59;}50%{stroke-dashoffset:-25;}100%{stroke-dashoffset:-109;}}
    @keyframes spark4 {0%{stroke-dashoffset:78;}50%{stroke-dashoffset:-42;}100%{stroke-dashoffset:-162;}}
    @keyframes spark5 {0%{stroke-dashoffset:60;}50%{stroke-dashoffset:-60;}100%{stroke-dashoffset:-180;}}
    @keyframes spark6 {0%{stroke-dashoffset:91;}50%{stroke-dashoffset:-29;}100%{stroke-dashoffset:-149;}}
    @keyframes spark7 {0%{stroke-dashoffset:60;}50%{stroke-dashoffset:-26;}100%{stroke-dashoffset:-112;}}
    @keyframes spark8 {0%{stroke-dashoffset:43;}50%{stroke-dashoffset:-43;}100%{stroke-dashoffset:-129;}}
    @keyframes spark9 {0%{stroke-dashoffset:60;}50%{stroke-dashoffset:-26;}100%{stroke-dashoffset:-112;}}

    /* WAVES */
    @keyframes wave1 {
        0%,25%,50%,75% {stroke-width:6; transform:scale(1);}
        10%,35%,60%,85%,100% {stroke-width:0; transform:scale(2);}
    }
                
    @keyframes wave1 {
        0%   { opacity:1; stroke-width:6; transform:scale(1);}
        100% { opacity:0; stroke-width:0; transform:scale(2.2);}
    }
                            
    @keyframes wave2 {
        5%,30%,55%,80% {stroke-width:6; transform:scale(1);}
        15%,40%,65%,90%,100% {stroke-width:0; transform:scale(2);}
    }

    </style>
    """, unsafe_allow_html=True)

    # ===== SVG ORIGINAL =====
    st.markdown("""
    <svg class="microchip" viewBox="0 0 128 128" width="128px" height="128px" role="img" aria-label="A square pops in emitting waves and lines, and sparks run through the lines">
        <symbol id="dot-1">
            <circle r="3" cx="3" cy="38" />
        </symbol>
        <symbol id="dot-2">
            <circle r="3" cx="3" cy="54" />
        </symbol>
        <symbol id="dot-3">
            <circle r="3" cx="3" cy="70" />
        </symbol>
        <symbol id="dot-4">
            <circle r="3" cx="3" cy="3" />
        </symbol>
        <symbol id="dot-5">
            <circle r="3" cx="20" cy="3" />
        </symbol>
        <symbol id="dot-6">
            <circle r="3" cx="3" cy="30" />
        </symbol>
        <symbol id="dot-7">
            <circle r="3" cx="37" cy="3" />
        </symbol>
        <symbol id="dot-8">
            <circle r="3" cx="54" cy="3" />
        </symbol>
        <symbol id="dot-9">
            <circle r="3" cx="71" cy="3" />
        </symbol>
        <symbol id="line-1">
            <polyline points="12 54,12 46,3 46,3 38" stroke-dasharray="42 42" />
        </symbol>
        <symbol id="line-2">
            <polyline points="29 54,3 54" stroke-dasharray="42 42" />
        </symbol>
        <symbol id="line-3">
            <polyline points="12 54,12 62,3 62,3 70" stroke-dasharray="42 42" />
        </symbol>
        <symbol id="line-4">
            <polyline points="28 20,28 12,20 12,20 3" stroke-dasharray="60 60" />
        </symbol>
        <symbol id="line-5">
            <polyline points="37 29,37 20,3 20,3 3" stroke-dasharray="60 60" />
        </symbol>
        <symbol id="line-6">
            <polyline points="15 20,15 30,3 30" stroke-dasharray="60 60" />
        </symbol>
        <symbol id="line-7">
            <polyline points="54 12,37 12,37 3" stroke-dasharray="43 43" />
        </symbol>
        <symbol id="line-8">
            <polyline points="54 29,54 3" stroke-dasharray="43 43" />
        </symbol>
        <symbol id="line-9">
            <polyline points="54 12,71 12,71 3" stroke-dasharray="43 43" />
        </symbol>
        <symbol id="spark-1">
            <polyline points="12 54,12 46,3 46,3 38" stroke-dasharray="15 69" />
        </symbol>
        <symbol id="spark-2">
            <polyline points="29 54,3 54" stroke-dasharray="15 69" />
        </symbol>
        <symbol id="spark-3">
            <polyline points="12 54,12 62,3 62,3 70" stroke-dasharray="15 69" />
        </symbol>
        <symbol id="spark-4">
            <polyline points="28 20,28 12,20 12,20 3" stroke-dasharray="15 105" />
        </symbol>
        <symbol id="spark-5">
            <polyline points="37 29,37 20,3 20,3 3" stroke-dasharray="15 105" />
        </symbol>
        <symbol id="spark-6">
            <polyline points="15 20,15 30,3 30" stroke-dasharray="15 105" />
        </symbol>
        <symbol id="spark-7">
            <polyline points="54 12,37 12,37 3" stroke-dasharray="15 71" />
        </symbol>
        <symbol id="spark-8">
            <polyline points="54 29,54 3" stroke-dasharray="15 71" />
        </symbol>
        <symbol id="spark-9">
            <polyline points="54 12,71 12,71 3" stroke-dasharray="15 71" />
        </symbol>
        <symbol id="wave">
            <rect x="3" y="3" rx="2.5" ry="2.5" width="44" height="44" />
        </symbol>
        <g transform="translate(10,10)">
            <g class="microchip__lines" stroke-linecap="round" stroke-linejoin="round">
                <g>
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--1" href="#line-1" />
                        <use class="microchip__spark microchip__spark--1" href="#spark-1" />
                        <use class="microchip__line microchip__line--2" href="#line-2" />
                        <use class="microchip__spark microchip__spark--2" href="#spark-2" />
                        <use class="microchip__line microchip__line--3" href="#line-3" />
                        <use class="microchip__spark microchip__spark--3" href="#spark-3" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--1" href="#dot-1" />
                        <use class="microchip__dot microchip__dot--2" href="#dot-2" />
                        <use class="microchip__dot microchip__dot--3" href="#dot-3" />
                    </g>
                </g>
                <g>
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--4" href="#line-4" />
                        <use class="microchip__spark microchip__spark--4" href="#spark-4" />
                        <use class="microchip__line microchip__line--5" href="#line-5" />
                        <use class="microchip__spark microchip__spark--5" href="#spark-5" />
                        <use class="microchip__line microchip__line--6" href="#line-6" />
                        <use class="microchip__spark microchip__spark--6" href="#spark-6" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--4" href="#dot-4" />
                        <use class="microchip__dot microchip__dot--5" href="#dot-5" />
                        <use class="microchip__dot microchip__dot--6" href="#dot-6" />
                    </g>
                </g>
                <g>
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--7" href="#line-7" />
                        <use class="microchip__spark microchip__spark--7" href="#spark-7" />
                        <use class="microchip__line microchip__line--8" href="#line-8" />
                        <use class="microchip__spark microchip__spark--8" href="#spark-8" />
                        <use class="microchip__line microchip__line--9" href="#line-9" />
                        <use class="microchip__spark microchip__spark--9" href="#spark-9" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--7" href="#dot-7" />
                        <use class="microchip__dot microchip__dot--8" href="#dot-8" />
                        <use class="microchip__dot microchip__dot--9" href="#dot-9" />
                    </g>
                </g>
                <g transform="translate(108,0) scale(-1,1)">
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--4" href="#line-4" />
                        <use class="microchip__spark microchip__spark--4" href="#spark-4" />
                        <use class="microchip__line microchip__line--5" href="#line-5" />
                        <use class="microchip__spark microchip__spark--5" href="#spark-5" />
                        <use class="microchip__line microchip__line--6" href="#line-6" />
                        <use class="microchip__spark microchip__spark--6" href="#spark-6" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--4" href="#dot-4" />
                        <use class="microchip__dot microchip__dot--5" href="#dot-5" />
                        <use class="microchip__dot microchip__dot--6" href="#dot-6" />
                    </g>
                </g>
                <g transform="translate(108,0) scale(-1,1)">
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--1" href="#line-1" />
                        <use class="microchip__spark microchip__spark--1" href="#spark-1" />
                        <use class="microchip__line microchip__line--2" href="#line-2" />
                        <use class="microchip__spark microchip__spark--2" href="#spark-2" />
                        <use class="microchip__line microchip__line--3" href="#line-3" />
                        <use class="microchip__spark microchip__spark--3" href="#spark-3" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--1" href="#dot-1" />
                        <use class="microchip__dot microchip__dot--2" href="#dot-2" />
                        <use class="microchip__dot microchip__dot--3" href="#dot-3" />
                    </g>
                </g>
                <g transform="translate(108,108) scale(-1,-1)">
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--4" href="#line-4" />
                        <use class="microchip__spark microchip__spark--4" href="#spark-4" />
                        <use class="microchip__line microchip__line--5" href="#line-5" />
                        <use class="microchip__spark microchip__spark--5" href="#spark-5" />
                        <use class="microchip__line microchip__line--6" href="#line-6" />
                        <use class="microchip__spark microchip__spark--6" href="#spark-6" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--4" href="#dot-4" />
                        <use class="microchip__dot microchip__dot--5" href="#dot-5" />
                        <use class="microchip__dot microchip__dot--6" href="#dot-6" />
                    </g>
                </g>
                <g transform="translate(0,108) scale(1,-1)">
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--7" href="#line-7" />
                        <use class="microchip__spark microchip__spark--7" href="#spark-7" />
                        <use class="microchip__line microchip__line--8" href="#line-8" />
                        <use class="microchip__spark microchip__spark--8" href="#spark-8" />
                        <use class="microchip__line microchip__line--9" href="#line-9" />
                        <use class="microchip__spark microchip__spark--9" href="#spark-9" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--7" href="#dot-7" />
                        <use class="microchip__dot microchip__dot--8" href="#dot-8" />
                        <use class="microchip__dot microchip__dot--9" href="#dot-9" />
                    </g>
                </g>
                <g transform="translate(0,108) scale(1,-1)">
                    <g fill="none" stroke="currentcolor">
                        <use class="microchip__line microchip__line--4" href="#line-4" />
                        <use class="microchip__spark microchip__spark--4" href="#spark-4" />
                        <use class="microchip__line microchip__line--5" href="#line-5" />
                        <use class="microchip__spark microchip__spark--5" href="#spark-5" />
                        <use class="microchip__line microchip__line--6" href="#line-6" />
                        <use class="microchip__spark microchip__spark--6" href="#spark-6" />
                    </g>
                    <g fill="currentcolor">
                        <use class="microchip__dot microchip__dot--4" href="#dot-4" />
                        <use class="microchip__dot microchip__dot--5" href="#dot-5" />
                        <use class="microchip__dot microchip__dot--6" href="#dot-6" />
                    </g>
                </g>
            </g>
            <g transform="translate(29,29)">
                <g class="microchip__center">
                    <g fill="none" stroke="currentcolor" stroke-width="6">
                        <use class="microchip__wave microchip__wave--1" href="#wave" />
                        <use class="microchip__wave microchip__wave--2" href="#wave" />
                    </g>
                    <rect class="microchip__core" fill="currentcolor" rx="5" ry="5" width="50" height="50" />
                </g>
            </g>
        </g>
    </svg>

    """, unsafe_allow_html=True)