# Exact Catalan hinge of the eight `H_4`-conjugate `D_4` boundary states

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let (s) be minimal with (C_s=\operatorname {Cat}_s\ge p), and put

\[
 H_4=\langle(2\ 3),(4\ 5),(6\ 7)\rangle.
\tag{0.1}
\]

On the canonical early parent slice, the four cells touched by the
six-start `D_4` boundary vector have the exact intrinsic loads

\[
 \boxed{
 L_2=C_s,\qquad L_3=C_{s-1},\qquad
 L_6=2C_{s-2},\qquad L_7=5C_{s-3}.}
\tag{0.2}
\]

Only (L_2) can meet or exceed (p); the other three are Catalan-
descending cells below cap.  Nevertheless no one of the eight direct
replacements (F\to hG) removes any occurrence from cell (2).  The
eight choices collapse to four signed vectors, each repeated twice:

\[
\begin{array}{c|rrrr|c}
(\epsilon_1,\epsilon_3)&\Delta_2&\Delta_3&\Delta_6&\Delta_7
 &\text{canonical cap gain for }s\ge5\\ \hline
(0,0)& 2&-3&-3& 4&-2\\
(1,0)& 0&-1&-3& 4& 0\\
(0,1)& 2&-3& 1& 0&-2\\
(1,1)& 0&-1& 1& 0& 0.
\end{array}
\tag{0.3}
\]

Here gain means old cap tail minus new cap tail.  The generator
((4\ 5)) has no effect on this profile, so each line represents two of
the eight states.

Thus the optimized direct state is neutral, not improving.  The tempting
vector with coefficient \(-3\) at the \(C_s\) source is obtained only by
conjugating the *difference* while silently leaving the old shore fixed.
It is the transition \(hF\to hG\), not \(F\to hG\).  For
\(\epsilon _1=1\), the preliminary move \(F\to hF\) first adds three
units to the source; the subsequent equivariant transition removes those
same three units.  Its apparent gain exactly repays the preliminary loss,
leaving the direct \(F\to hG\) state neutral.

Consequently no `H_4` conjugate of this finite factor repairs the
hereditary (C_s) source.  Along a chain of (L) aligned depths, the best
direct (F\to hG) choice has gain (0), whereas the unflipped choices
lose (2L).  Any positive result must add a state outside this conjugacy
orbit, use reversal/non-coordinate mixing with a genuinely negative source
coefficient, or obtain gain from other background-overloaded collar cells;
it cannot come from the canonical Catalan source itself.

## 1. Exact canonical cell loads

In a parent of semilength (s+1), the canonical MSW boundary census is

\[
 w_j=C_{j-1}C_{s+1-j},\qquad1\le j\le s+1.
\tag{1.1}
\]

The even boundary copy puts (w_j) occurrences at local target (2j),
and the odd boundary copy puts the same number at target (2j-1).  This is
the first-return decomposition: if the first return cuts off a Dyck word
of semilength (j-1), the two free pieces have respectively
(C_{j-1}) and (C_{s+1-j}) choices.

Taking (j=1,2,3,4) gives

\[
\begin{aligned}
 \mu(2)&=w_1=C_s,\\
 \mu(3)&=w_2=C_{s-1},\\
 \mu(6)&=w_3=C_2C_{s-2}=2C_{s-2},\\
 \mu(7)&=w_4=C_3C_{s-3}=5C_{s-3},
\end{aligned}
\tag{1.2}
\]

which proves (0.2).  Along a one-sided hereditary chain the exterior core
(K_q) changes, but the local first-return census does not, so (1.2)
holds on the physical cells (K_q\cup\{2\},K_q\cup\{3\},
K_q\cup\{6\},K_q\cup\{7\}) at every surviving depth.

Minimality of (s) gives

\[
 C_{s-1}<p\le C_s,
 \qquad
 1\le\theta={C_s\over p}
 <{C_s\over C_{s-1}}
 =4-{6\over s+1}.
\tag{1.3}
\]

Moreover, for (s\ge5),

\[
 2C_{s-2}+4\le p,qquad5C_{s-3}+4\le p.
\tag{1.4}
\]

Indeed (p\ge C_{s-1}+1), while

\[
 C_{s-1}-2C_{s-2}\ge4,qquad
 C_{s-1}-5C_{s-3}\ge4
\tag{1.5}
\]

at (s=5), and both gaps increase thereafter.  Thus additions of size at
most four to cells (6,7) remain below cap throughout the asymptotic
early-scale regime.

For reference, the exact normalized lower loads are

\[
 {L_3\over p}
 =\theta {s+1\over2(2s-1)},
\tag{1.6}
\]

\[
 {L_6\over p}
 =\theta {s(s+1)\over2(2s-1)(2s-3)},
\tag{1.7}
\]

and

\[
 {L_7\over p}
 =\theta {5s(s-1)(s+1)
       \over8(2s-1)(2s-3)(2s-5)}.
\tag{1.8}
\]

They tend respectively to (	heta/4,	heta/8,5\theta/64).

## 2. The correct eight direct transitions (F\to hG)

On the six open-parent starts, the canonical and new local packet
histograms, restricted to (2,3,6,7), are

\[
 u_F=(9,12,12,9),\qquad u_G=(11,9,9,13).
\tag{2.1}
\]

Let

\[
 h=(2\ 3)^{\epsilon_1}(4\ 5)^{\epsilon_2}
        (6\ 7)^{\epsilon_3}.
\tag{2.2}
\]

Reanchoring permutes the roots but does not alter the aggregate histogram,
so the direct replacement of the fixed canonical packet by (hG) has

\[
                         \Delta^h=h_*u_G-u_F.
\tag{2.3}
\]

Because both factors have load twelve at (4,5), the bit
(epsilon_2) is inert here.  Literal subtraction gives (0.3):

\[
\begin{array}{c|rrrr}
(\epsilon_1,\epsilon_3)&2&3&6&7\\ \hline
(0,0)& 2&-3&-3&4\\
(1,0)& 0&-1&-3&4\\
(0,1)& 2&-3&1&0\\
(1,1)& 0&-1&1&0.
\end{array}
\tag{2.4}
\]

In particular

\[
                         \Delta^h(2)\in\{0,2\}
\tag{2.5}
\]

for every (h).  No direct state removes load from the (C_s) cell.

## 3. Exact hinge optimization

For a load (x), define

\[
 R_k(x)=(x-p)_+-(x-k-p)_+,
 \qquad
 A_k(x)=(x+k-p)_+-(x-p)_+.
\tag{3.1}
\]

These are respectively the cap gain from removing (k) units and the cap
loss from adding (k) units.  Put

\[
 a=C_s,quad b=C_{s-1},quad c=2C_{s-2},quad d=5C_{s-3}.
\tag{3.2}
\]

The old-minus-new cap gains of the four rows of (2.4) are exactly

\[
\begin{aligned}
 g_{00}&=-A_2(a)+R_3(b)+R_3(c)-A_4(d),\\
 g_{10}&=R_1(b)+R_3(c)-A_4(d),\\
 g_{01}&=-A_2(a)+R_3(b)-A_1(c),\\
 g_{11}&=R_1(b)-A_1(c).
\end{aligned}
\tag{3.3}
\]

For (s\ge5), equations (1.3)--(1.5) give

\[
 A_2(a)=2,quad R_k(b)=R_k(c)=0,quad
 A_4(d)=A_1(c)=0.
\tag{3.4}
\]

Therefore

\[
                         \boxed{(g_{00},g_{10},g_{01},g_{11})
                                      =(-2,0,-2,0).}
\tag{3.5}
\]

This is exact and uniform over the whole admissible overshoot interval
(1\le\theta<4-6/(s+1)).  It includes (	heta=1): adding two units to a
cell exactly at cap creates two units of overload.

If the same carrier profile survives through a chain (mathcal Q) of
(L=|\mathcal Q|) depths, the single common factor choice gives

\[
                \boxed{G_{00}=G_{01}=-2L,qquad
                       G_{10}=G_{11}=0.}
\tag{3.6}
\]

Thus the optimum over all eight conjugates is zero.

The finite exceptional scale (s=4) changes only the term (A_4(d)):
(d=5), so the two rows with (epsilon_3=0) incur the additional loss
((9-p)_+).  The (epsilon_3=1) rows, and in particular the neutral
((1,1)) row, retain the conclusions above.

## 4. Why conjugating the signed vector gives no net drain from F

The equivariant difference between equally conjugated shores is

\[
 h_*(u_G-u_F).
\tag{4.1}
\]

On (2,3,6,7), its four distinct values are

\[
\begin{array}{c|rrrr}
(\epsilon_1,\epsilon_3)&2&3&6&7\\ \hline
(0,0)& 2&-3&-3&4\\
(1,0)&-3& 2&-3&4\\
(0,1)& 2&-3&4&-3\\
(1,1)&-3& 2&4&-3.
\end{array}
\tag{4.2}
\]

The last two rows with \(\epsilon_1=1\) appear to remove three units from
the fixed \(C_s\) cell \(2\) and add them only to lower Catalan cells.
This is a real gain for the transition \(hF\to hG\), but its old state is
not the canonical state \(F\).  Relative to \(F\), installing \(hF\) on
the packet first changes the pair-\(1\) contribution by

\[
                         (+3,-3),
\tag{4.3}
\]

so it adds three units to the already overloaded source cell.  The
transition \(hF\to hG\) then has pair-\(1\) vector \((-3,+2)\): it removes
the three newly added source units and leaves the descending cell one unit
below its canonical load.  Thus, on the canonical Catalan slice,

\[
 \operatorname {gain}(F\to hF)=-3,\qquad
 \operatorname {gain}(hF\to hG)=+3,\qquad
 \operatorname {gain}(F\to hG)=0.
\tag{4.4}
\]

For \(\epsilon_1=0\), no such intermediate relocation occurs and the
direct/equivariant transition loses two units.  The lower-pair changes
remain inside the slack from (1.4).

Algebraically,

\[
 (h_*u_F-u_F)+h_*(u_G-u_F)=h_*u_G-u_F,
\tag{4.5}
\]

whose source coordinate is zero when \(\epsilon_1=1\), exactly as in
(2.4).  This is why the putative drain disappears after measuring from
the canonical state.

## 5. Background and PCap qualification

Equations (0.2)--(3.6) concern the intrinsic canonical boundary slice.  If
other contexts put background \(\beta_{q,x}\) on the same physical cells,
replace \(a,b,c,d\) in (3.3) by

\[
 a+\beta_{q,2},\quad b+\beta_{q,3},\quad
 c+\beta_{q,6},\quad d+\beta_{q,7}
\tag{5.1}
\]

and sum (3.3) over (q).  The resulting formula is still exact, but a
descending cell may then be overloaded and a removal there can create
incidental gain.  Such gain is not repair of the (C_s) source, because
(2.5) remains true with arbitrary background.

For the outer PCap summand

\[
 [K_p(\mu_q)-(W-N_q)]_+,
\tag{5.2}
\]

the cap-tail changes above transfer verbatim while both old and new values
are on the active branch.  Off that branch they are truncated toward zero,
so a neutral or losing direct state cannot become a certified positive
source drain.

Finally, this audit covers the six-start boundary slice.  The three
attachment starts carry the compensating profile, and a common physical
carrier for all nine starts cancels the complete singleton action.  At
higher local carrier lengths the full row/start tensor remains mandatory.
Thus the `H_4` no-drain result is already decisive for the proposed
(C_s)-source mechanism, while a global PCap theorem would still have to
audit every collar profile of any larger replacement library.
