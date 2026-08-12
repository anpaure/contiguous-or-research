# Lane U7: equal-ray PACK and multipin middle absorption

Date: 2026-07-25

## 0. Verdict

Let

\[
 \mathcal A_r=[0,r]^2\times H_r,
 \qquad
 \mathcal B_r=H_r\times
 \bigl(\{1,\ldots,r\}\times\{0,\ldots,r-1\}\bigr),
\]

where

\[
 h_t=
 \begin{cases}
 (0,t),&0\le t\le r,\\
 (t-r,r),&r\le t\le2r,
 \end{cases}
 \qquad H_r=\{h_0<\cdots<h_{2r}\}.
\]

The aligned packet-middle antichain has size

\[
 W_r=(r+1)^2+r^2=2r^2+2r+1.
\tag{0.1}
\]

The full complementary packet theorem

\[
 g(\mathcal A_r\mathbin{\dot\cup}\mathcal B_r)
 \le W_r+o(r^2)
\tag{PACK}
\]

is **not proved** here.  The exact multipin middle obstruction, however,
is resolved positively, and the obstruction moves strictly deeper.

This report proves the following new statements.

1. Every one of the \(r^2\) aligned \(\mathcal B_r\)-middle targets is
   covered by adjacent pairs in one alternating
   \(\mathcal A_r/\mathcal B_r\) carrier word of length
   \[
   \begin{cases}
   r^2+r,&r\text{ odd},\\
   r^2+r-1,&r\text{ even}.
   \end{cases}
   \tag{0.2}
   \]
   At least \(r(r-2)\) distinct targets have a genuinely multipin
   factorization: the \(\mathcal A_r\)-endpoint is deficient in the third
   coordinate and also in the hook or fourth coordinate.  A quadratic
   number of physical carrier sites are simultaneously a right endpoint
   of one selected owner and a left endpoint of a distinct selected owner.
   Appending the
   \(\mathcal A_r\)-middle targets literally covers the whole aligned
   middle layer in length
   \[
   W_r+r-\mathbf 1_{2\mid r}.
   \tag{0.3}
   \]
   Thus neither coordinate pins, endpoint acyclicity, nor the verified
   one-pin completion bound is an obstruction at the middle sheet.

2. A second explicit atlas of length
   \[
   W_r+2r
   \tag{0.4}
   \]
   covers all aligned middle targets and a certified family of exactly
   \[
   \frac{(r+1)^2(r+2)}2
   +\frac{r^2(r+1)}2
   \tag{0.5}
   \]
   packet targets on a literal half-upper surface.  (Additional within-block
   and cross-block maxima are not counted.)  This is
   \(\Theta(r^3)\) target coverage at only linear excess, not merely a
   middle-layer certificate.

3. Every full packet word satisfies the new exact unrestricted lower
   bound
   \[
   \boxed{g(\mathcal A_r\mathbin{\dot\cup}\mathcal B_r)\ge W_r+r.}
   \tag{0.6}
   \]
   This is compatible with PACK, since \(r=o(r^2)\), but it gives an exact
   universal linear floor.  No matching full-packet upper bound is claimed.

4. Arbitrary multipins do not repair the *immutable* displayed
   common-lift matching.  With
   \[
   k_r=\left\lfloor\frac{r-1}{8}\right\rfloor,
   \]
   if every useful middle absorption is required to retain the one
   preassigned side-typed incidence at its displayed matching site, then
   \[
   e\ge
   \max\left\{0,
   \left\lceil
   \frac{\Gamma_r-\bigl((k_r+1)r-k_r(k_r+1)/2\bigr)}4
   \right\rceil\right\}
   =\frac{173}{13824}r^2+O(r).
   \tag{0.7}
   \]
   This uses only rank and therefore includes owners changing arbitrarily
   many coordinates.  A successful PACK braid must replace a positive
   density of the displayed physical portal incidences, not merely wrap
   multipin middle witnesses around the old common-lift order.

5. A diagonal two-sided multipin path braid makes that replacement at the
   middle level with \(O(r)\) excess.  But retaining its chronology while
   restoring the selected source-gap common-lift child witnesses requires
   exactly
   \[
   (r-1)(\lceil r/2\rceil-1)=\Theta(r^2)
   \tag{0.8}
   \]
   inserted positions.  Hence the surviving operation is a genuinely
   hybrid order which preserves neither already known chronology
   unchanged.

No implication to the constant-one theorem is claimed.  No finite search,
computation, or nonliteral synchronization is used.

---

## 1. Packet ranks and exact counts

Write (|x|) for ambient coordinate sum.  The packet rank generating
polynomials are

\[
 P_{\mathcal A_r}(z)=P_r(z)^2P_{2r}(z),
 \qquad
 P_{\mathcal B_r}(z)=zP_{2r}(z)P_{r-1}(z)^2.
\tag{1.1}
\]

Both are symmetric about ambient rank (2r).  Their middle coefficients
are respectively

\[
 (r+1)^2,
 \qquad r^2,
\tag{1.2}
\]

which proves (0.1).

For later interface formulas write

\[
 a_{t,v}:=(h_t;0,v),
 \qquad
 b_{t,v}:=(h_t;1,v).
\tag{1.2a}
\]

Every (\mathcal B_r)-middle target has the unique form

\[
 T_{u,v}:=(h_{2r-u-v};u,v),
 \qquad
 1\le u\le r,\qquad0\le v\le r-1.
\tag{1.3}
\]

The hook index lies in ([1,2r-1]), so all (r^2) displayed points are
legal and distinct.

The numbers of nonzero targets below rank (2r) will be used later.  For
(\mathcal A_r), symmetry gives

\[
 L_A^-=
 \frac{(r+1)^2(2r+1)-(r+1)^2}{2}-1
 =r(r+1)^2-1.
\tag{1.4}
\]

The final (-1) removes the ambient zero.  For (\mathcal B_r),

\[
 L_B^-=
 \frac{(2r+1)r^2-r^2}{2}=r^3.
\tag{1.5}
\]

Thus

\[
 \boxed{L_r^-:=L_A^-+L_B^-
 =2r^3+2r^2+r-1.}
\tag{1.6}
\]

Directly, (1.5) is also

\[
 \sum_{u=1}^r\sum_{v=0}^{r-1}(2r-u-v)=r^3,
\tag{1.7}
\]

because there are exactly (2r-u-v) hook indices below the middle hook
index in (1.3).

---

## 2. An alternating multipin braid for every (\mathcal B_r)-middle target

### 2.1 The parity-corrected snake

For (1\le u\le r), let the (u)-th row be

\[
 R_u=
 \begin{cases}
 (T_{u,0},T_{u,1},\ldots,T_{u,r-1}),&u\text{ odd},\\
 (T_{u,r-1},T_{u,r-2},\ldots,T_{u,0}),&u\text{ even}.
 \end{cases}
\tag{2.1}
\]

Modify the concatenation of these rows as follows.

- If (r) is odd, after every row (R_u) with (u<r), repeat its last
  target once.
- If (r) is even, after every even row (R_u) with (u<r), repeat its
  last target twice; after odd rows make no repetition.

Call the resulting target list

\[
 \mathcal T_r=(T_1,T_2,\ldots,T_m).
\tag{2.2}
\]

Its exact length is

\[
 m=
 \begin{cases}
 r^2+r-1,&r\text{ odd},\\
 r^2+r-2,&r\text{ even}.
 \end{cases}
\tag{2.3}
\]

Indeed, the odd case adds (r-1) copies.  In the even case, there are
(r/2-1) even rows strictly before the last row, and each adds two copies.

Every row starts at an odd list index.  In the odd case each completed
row-plus-repeat has even length (r+1).  In the even case each row has
even length (r), and the optional two repetitions preserve even parity.

### 2.2 Meet carriers

Put

\[
 D_0=T_1,
 \qquad
 D_i=T_i\wedge T_{i+1}\quad(1\le i<m),
 \qquad
 D_m=T_m.
\tag{2.4}
\]

Every (D_i) has the form

\[
 D_i=(h_{s_i};\mu_i,\nu_i).
\]

Define the physical carrier

\[
 C_i=
 \begin{cases}
 D_i,&i\text{ odd},\\
 (h_{s_i};0,\nu_i),&i\text{ even}.
 \end{cases}
\tag{2.5}
\]

The odd carriers lie in (\mathcal B_r).  The even carriers lie in
(\mathcal A_r), because ((0,\nu_i)\in H_r).  All are nonzero: every
hook index appearing in (1.3), and hence in a meet of adjacent targets in
this list, is at least one unless the fourth coordinate is already
positive.

### Lemma 2.1 (literal meet identity)

For every (1\le i\le m),

\[
 \boxed{C_{i-1}\vee C_i=T_i.}
\tag{2.6}
\]

#### Proof

First ignore the replacement in (2.5).  Along one row, the hook index and
the fourth coordinate move monotonically in opposite directions and the
third coordinate is constant.  At a high-(v) row turn, each coordinate
of the turning target is attained by it and at least one neighbor.  At a
low-(v) turn, the repeated row-end target supplies the same property.
Every inserted copy has an equal neighbor.  At the two ends it is supplied
by the convention (D_0=T_1,D_m=T_m).  Therefore, coordinate by
coordinate,

\[
 (T_{i-1}\wedge T_i)\vee(T_i\wedge T_{i+1})=T_i,
\tag{2.7}
\]

with the evident endpoint interpretation.

It remains to check the third coordinate after (2.5).  Exactly one of
(i-1,i) is odd.  If (i) is odd, the retained right meet (D_i) has
third coordinate (u_i): the right neighbor is in the same row, is a
row-end copy, or is in the next row and has larger (u).  If (i) is
even, then (i) is not a row start, because all row starts are odd.  Its
left neighbor therefore has the same (u_i), and the retained left meet
(D_{i-1}) has third coordinate (u_i).  Thus zeroing the third
coordinate of the even meet does not change the join.  No other coordinate
was changed, so (2.6) follows from (2.7). \(\square\)

### Theorem 2.2 (equal-ray multipin middle absorption)

For every (r\ge1), the word

\[
 \mathcal C_r=C_0,C_1,\ldots,C_m
\tag{2.8}
\]

covers every target of the (\mathcal B_r)-middle antichain.  Its length
is

\[
 \boxed{
 |\mathcal C_r|=
 \begin{cases}
 r^2+r,&r\text{ odd},\\
 r^2+r-1,&r\text{ even}.
 \end{cases}}
\tag{2.9}
\]

For (r\ge3), at least (r(r-2)) distinct middle targets use a selected
two-letter witness whose even (\mathcal A_r)-carrier differs from its
owner in at least two ambient coordinates.

Moreover the number of internal even carrier positions, counted in the
listed witness system (which includes repeated row-end target occurrences),
is exactly

\[
 P_r=
 \begin{cases}
 (r^2+r-2)/2,&r\text{ odd},\\
 (r^2+r-4)/2,&r\text{ even}.
 \end{cases}
\tag{2.10}
\]

If one selects only one witness for each **distinct** middle owner, the
displayed transition system certifies the following exact number of even
sites which remain a right endpoint for one owner and a left endpoint for
a different owner:

\[
 P_r^{\mathrm{dist}}=
 \begin{cases}
 (r^2+r-2)/2,&r\text{ odd},\\
 r^2/2-1,&r\text{ even}.
 \end{cases}
\tag{2.10a}
\]

#### Proof

Every distinct (T_{u,v}) occurs in the snake, and (2.6) gives it an
actual adjacent-pair witness.  Formula (2.9) is (2.3) plus one.

Fix (1\le v\le r-2).  The target (T_{u,v}) is not a row endpoint.  Its
even carrier is the meet with one of its two within-row neighbors, followed
by zeroing the third coordinate.  If the neighbor has fourth coordinate
(v+1), the meet loses hook height; if it has fourth coordinate (v-1),
the meet loses fourth-coordinate height.  In both cases it also loses the
positive third coordinate (u).  Hence all (r(r-2)) such targets have a
genuine multipin factorization.

Finally, the internal carrier indices are \(1,\ldots,m-1\).  Counting the
even indices in that range and inserting the two parities of (2.3) gives
(2.10).  At such an index \(i\), the same physical occurrence \(C_i\) is
the right endpoint of \([C_{i-1},C_i]\) and the left endpoint of
\([C_i,C_{i+1}]\).  When \(r\) is even, exactly \(r/2-1\) of these sites
lie between repeated copies of one row-end owner.  Select the last-copy
adjacent witness at each such triple-copy seam; precisely that same-owner
even site is then lost, giving (2.10a).  In the odd case a seam has two
copies of its row-end owner and the carrier between them is odd.  Replace
the two duplicate adjacent witnesses by the single three-carrier interval
from the even carrier immediately before that odd carrier to the even
carrier immediately after it.  Its maximum is the repeated owner, and
both even boundary sites remain exposed to the distinct outer neighbors.
Thus no even site is lost in the odd case.  This proves the certified
count (2.10a); it is not asserted to be a maximum over all possible
witness systems. \(\square\)

### Corollary 2.3 (the whole aligned middle sheet)

Append one literal singleton for every (\mathcal A_r)-middle target to
\(\mathcal C_r\).  The resulting one word covers all (W_r) aligned
middle targets and has exact length

\[
 \boxed{W_r+r-\mathbf 1_{2\mid r}.}
\tag{2.11}
\]

This is the requested positive middle-absorption mechanism.  It evades the
one-pin theorem in two literal ways: it does not retain the whole
designated (F_A) spine, and its positive-density interior owners split
their missing coordinates between two dynamically chosen carrier sites.

---

## 3. A \(W_r+2r\) half-upper atlas

The middle braid above is not an isolated rank trick.  The following word
covers a cubic family of actual packet targets.

### 3.1 The (\mathcal B_r) blocks

For every (1\le u\le r), define a block of (r+1) letters

\[
 C_{u,0}=(h_{2r-u};0,0),
\tag{3.1}
\]

and, for (1\le j\le r),

\[
 C_{u,j}=
 \begin{cases}
 (h_{2r-u-j};u,j-1),&j\text{ odd},\\
 (h_{2r-u-j};0,j-1),&j\text{ even}.
 \end{cases}
\tag{3.2}
\]

Odd letters lie in (\mathcal B_r), and even letters lie in
(\mathcal A_r).  All hook indices are in ([0,2r]).

If (0\le a\le b\le r) and the interval contains an odd index, then

\[
 \bigvee_{j=a}^b C_{u,j}
 =(h_{2r-u-a};u,b-1),
\tag{3.3}
\]

with the natural interpretation at (a=0).  In particular, every target

\[
 (h_t;u,v)\in\mathcal B_r,
 \qquad
 t+u+v\ge2r,
 \qquad
 t\le2r-u,
\tag{3.4}
\]

is covered.  If (t=2r-u), use the interval from (C_{u,0}) through
(C_{u,v+1}).  Otherwise put

\[
 a=2r-u-t,
 \qquad b=v+1.
\]

The rank condition gives (1\le a\le v<b), so the interval contains two
consecutive indices and therefore an odd one.  Formula (3.3) gives the
target exactly.

For fixed (u,v), the allowed hook indices in (3.4) number (v+1).
Consequently the certified family in (3.4) has exactly

\[
 \boxed{N_B^+=r\sum_{v=0}^{r-1}(v+1)
 =\frac{r^2(r+1)}2}
\tag{3.5}
\]

distinct \(\mathcal B_r\)-targets, all covered by the blocks, which use
\(r(r+1)\) letters.  Singleton and other intervals may cover additional
targets not counted in (3.5).

### 3.2 The (\mathcal A_r) blocks

For (0\le x\le r), put

\[
 P_x=
 \begin{cases}
 (0,0;h_{2r}),&x=0,\\
 (x-1,0;h_{2r-x}),&1\le x\le r,
 \end{cases}
\tag{3.6}
\]

and, for (0\le y\le r), put

\[
 E_{x,y}=(x,y;h_{2r-x-y-1}),
\tag{3.7}
\]

except at the single formal negative-index corner, where

\[
 E_{r,r}:=(r-1,r;h_0).
\tag{3.8}
\]

Use the block

\[
 P_x,E_{x,0},E_{x,1},\ldots,E_{x,r}.
\tag{3.9}
\]

Every letter lies in (\mathcal A_r).  Let

\[
 (x,y;h_q)\in\mathcal A_r,
 \qquad
 x+y+q\ge2r,
 \qquad
 q\le2r-x.
\tag{3.10}
\]

If (q=2r-x), the interval from (P_x) through (E_{x,y}) has maximum
((x,y;h_q)).  If (q<2r-x), set

\[
 a=2r-x-q-1.
\tag{3.11}
\]

The rank condition gives (0\le a\le y-1), and the interval

\[
 E_{x,a},E_{x,a+1},\ldots,E_{x,y}
\]

has maximum ((x,y;h_q)).  At ((x,y)=(r,r)), the preceding ordinary
letter (E_{r,r-1}) still pins the first coordinate (r), while the
special last letter (3.8) pins the second coordinate (r); the same join
calculation remains valid.

For fixed (x,y), the permitted hook indices in (3.10) number (y+1).
Thus the certified family in (3.10) has exactly

\[
 \boxed{N_A^+=(r+1)\sum_{y=0}^r(y+1)
 =\frac{(r+1)^2(r+2)}2}
\tag{3.12}
\]

distinct \(\mathcal A_r\)-targets, all covered by the blocks, which use
\((r+1)(r+2)\) letters.  Additional maxima are not counted in (3.12).

### Theorem 3.1 (literal half-upper atlas)

For every \(r\ge1\), order the \(\mathcal A_r\)-blocks by increasing \(x\)
first and the \(\mathcal B_r\)-blocks by increasing \(u\) second, and
identify their common boundary letter

\[
 E_{r,r}=(r-1,r;h_0)=(h_{2r-1};0,0)=C_{1,0}.
\tag{3.12a}
\]

This gives one nonzero ambient word of length

\[
 \boxed{
 r(r+1)+(r+1)(r+2)-1
 =W_r+2r}
\tag{3.13}
\]

which covers all targets in (3.4) and (3.10).  Their exact total number is
(0.5), and the family contains every aligned packet-middle target.

#### Proof

The only witnesses used are the literal intervals verified in (3.3) and
(3.9)--(3.11).  The identification (3.12a) is simultaneously the last
letter of the final \(\mathcal A_r\)-block and the first letter of the
initial \(\mathcal B_r\)-block, so it inserts or deletes nothing inside
either certified interval.  A middle \(\mathcal B_r\)-target has
(t=2r-u-v\le2r-u), and a middle (\mathcal A_r)-target has
(q=2r-x-y\le2r-x).  Hence all middle targets occur.  The length and
target counts are (3.5), (3.12), and direct addition. \(\square\)

The missing upper caps are exact:

\[
 q>2r-x\quad\text{in }\mathcal A_r,
 \qquad
 t>2r-u\quad\text{in }\mathcal B_r.
\tag{3.14}
\]

The entire lower half is also not covered.  Reversing either block family
produces another near-width atlas, but concatenating the two pays a
quadratic baseline twice.  No reset-free common refinement of the two
orientations is proved here.

---

## 4. An exact unrestricted linear lower bound for PACK

### Theorem 4.1

For every integer (r\ge1), every word covering every nonzero target in
(\mathcal A_r\mathbin{\dot\cup}\mathcal B_r) has length at least

\[
 \boxed{W_r+r.}
\tag{4.1}
\]

#### Proof

Let the word length be

\[
 n=W_r+e.
\tag{4.2}
\]

The aligned middle targets form an antichain, so (e\ge0).  Choose one
witness

\[
 I_i=[\ell_i,r_i]
\]

for each of the (W_r) middle targets, and order them by increasing left
endpoint.  Left endpoints are distinct: two intervals with a common left
endpoint are nested and have comparable maxima.  The same nesting
argument shows that the right endpoints are distinct and occur in the same
order.  Thus

\[
 \ell_i=i+\alpha_i,
 \qquad
 r_i=i+\beta_i,
\tag{4.3}
\]

where

\[
 0\le\alpha_1\le\cdots\le\alpha_{W_r}\le e,
 \qquad
 0\le\beta_1\le\cdots\le\beta_{W_r}\le e.
\]

Put (d_i=r_i-\ell_i\).  Then

\[
 0\le d_i\le e,
 \qquad
 \sum_i d_i\le W_re.
\tag{4.4}
\]

Choose one witness for every nonzero packet target of rank below (2r),
and group these witnesses by left endpoint.  At a selected middle start
(\ell_i), such a witness must end strictly before (r_i); otherwise it
contains (I_i), and its maximum dominates a rank-(2r) target, impossible
for a lower-rank maximum.  Hence at most (d_i) lower targets use that
start.

There are exactly (e) word positions which are not selected middle left
endpoints.  At any one fixed start, interval maxima obtained by moving the
right endpoint form a chain.  A strict chain of nonzero targets below rank
(2r) has at most (2r-1) elements.  Therefore (1.6) and (4.4) give

\[
 L_r^-
 \le\sum_i d_i+(2r-1)e
 \le(W_r+2r-1)e
 =(2r^2+4r)e.
\tag{4.5}
\]

Now

\[
 L_r^-=(r-1)(2r^2+4r)+(5r-1),
\tag{4.6}
\]

and

\[
 0<5r-1<2r^2+4r
 \qquad(r\ge1).
\]

Integrality in (4.5) yields (e\ge r), proving (4.1). \(\square\)

The theorem is unrestricted: letters may lie anywhere in the ambient
four-box, middle witnesses may be arbitrarily long, and every coordinate
may have arbitrarily many physical pins.  Its scale is only linear, so it
does not refute PACK.

---

## 5. Arbitrary multipins cannot preserve the displayed common-lift matching

This section retains the exact endpoint toll notation from the audited
common-lift report.  Put

\[
 k=k_r=\left\lfloor\frac{r-1}{8}\right\rfloor.
\tag{5.1}
\]

The displayed sloped matching sites are

\[
 X_{x,v}=((x,r);0,v),
 \qquad
 x+v=r+\sigma,
 \qquad
 -k\le\sigma\le k,
\tag{5.2}
\]

with (1\le x\le r), (0\le v\le r-1).  There are (r-|\sigma|)
sites at slope (\sigma).  The U5 word assigns exactly one side type to
each displayed matching incidence.

The exact two-child endpoint toll is

\[
 \Gamma_r=\gamma_A(r)+\gamma_B(r),
\tag{5.3}
\]

where

\[
 \gamma_A(r)=
 \max\left\{0,
 \left\lceil
 \frac{
 2k(r+1)^2+k(k+1)(k-12r-4)/3
 }{2r+2k}
 \right\rceil\right\},
\tag{5.4}
\]

\[
 \gamma_B(r)=
 \max\left\{0,
 \left\lceil
 \frac{
 (2+2k)r^2+k(k+1)(k-12r+8)/3
 }{2r+2k}
 \right\rceil\right\}.
\tag{5.5}
\]

Thus

\[
 \Gamma_r=\frac{289}{1728}r^2+O(r).
\tag{5.6}
\]

For a packet word of length (W_r+e), choose all middle witnesses and the
two selected band witness families.  If (a) denotes their side-typed
same-side absorption count, the audited endpoint ledger is

\[
 \boxed{4e+a\ge\Gamma_r.}
\tag{5.7}
\]

### Theorem 5.1 (immutable matching obstruction, arbitrary multipin)

Let \(r\ge2\).  Suppose every incidence counted by \(a\) is required to
be the one preassigned side-typed incidence at a displayed physical site
(5.2), and suppose that site retains the literal letter \(X_{x,v}\).
The middle owner above that site may differ in any number of coordinates.
Then

\[
 a\le A_r^-:=(k+1)r-\frac{k(k+1)}2,
\tag{5.8}
\]

and consequently

\[
 \boxed{
 e\ge
 \max\left\{0,
 \left\lceil\frac{\Gamma_r-A_r^-}{4}\right\rceil
 \right\}
 =\frac{173}{13824}r^2+O(r).}
\tag{5.9}
\]

#### Proof

The site (X_{x,v}) has rank

\[
 |X_{x,v}|=r+x+v=2r+\sigma.
\]

If it is a letter in a witness whose maximum is a rank-(2r) middle
target (M), then (X_{x,v}\le M), so necessarily (\sigma\le0).
This argument does not inspect how many coordinates differ between the
letter and (M).

Because the architecture retains only the one preassigned side type at
each displayed site, the total eligible incidence count is

\[
 \sum_{d=0}^k(r-d)
 =(k+1)r-\frac{k(k+1)}2,
\]

which proves (5.8).  Insert (5.8) into (5.7).  Since

\[
 A_r^-=\frac{15}{128}r^2+O(r),
\]

we have

\[
 \frac14\left(\frac{289}{1728}-\frac{15}{128}\right)
 =\frac14\cdot\frac{173}{3456}
 =\frac{173}{13824},
\]

proving (5.9). \(\square\)

The side-type hypothesis is essential.  A new word may use one physical
site as a right middle endpoint and a left middle endpoint for two
different owners; Theorem 2.2 does exactly this.  The conclusion of
Theorem 5.1 is therefore not an unrestricted PACK lower bound.  It proves
that merely adding arbitrary multipin providers around the immutable U5
matching does not work.

---

## 6. A two-sided diagonal braid and its exact selected hybrid tax

The next construction makes the two-sided escape completely explicit and
then audits a quadratic selected family which prevents it from simply
being inserted into the common-lift word.

Put

\[
 m=\left\lceil\frac r2\right\rceil.
\tag{6.1}
\]

For (1\le d\le r), (0\le j<m), define

\[
 P_{d,j}:=a_{2r-d-2j,\,2j}
 =(h_{2r-d-2j};0,2j).
\tag{6.2}
\]

For (2\le d\le r), (0\le j<m-1), define

\[
 q_{d,j}:=(h_0;d-1,2j+1).
\tag{6.3}
\]

Then

\[
 P_{d,j}\vee q_{d,j}
 =(h_{2r-d-2j};d-1,2j+1),
\tag{6.4}
\]

\[
 q_{d,j}\vee P_{d-1,j+1}
 =(h_{2r-d-2j-1};d-1,2j+2).
\tag{6.5}
\]

Both are legal (\mathcal B_r)-middle targets.  The two displayed target
families are disjoint because their fourth coordinates have opposite
parity, and they are internally injective.

The directed transitions

\[
 (d,j)\longrightarrow(d-1,j+1)
\tag{6.6}
\]

form a path forest on (rm) portal vertices.  It has

\[
 E=(r-1)(m-1)
\tag{6.7}
\]

edges and therefore

\[
 C=rm-E=r+m-1
\tag{6.8}
\]

components.  Along each component, write the alternating word

\[
 P,q,P,q,\ldots,P.
\]

It has (2E+C) letters and covers the (2E) distinct middle targets in
(6.4)--(6.5).  Append every other packet-middle target literally.  The
resulting word covers the whole aligned middle layer and has exact length

\[
 (2E+C)+(W_r-2E)
 =\boxed{W_r+r+\left\lceil\frac r2\right\rceil-1}.
\tag{6.9}
\]

Every portal with

\[
 2\le d\le r-1,
 \qquad1\le j\le m-2
\]

is internal to its path and is simultaneously a right and left middle
endpoint.  For (r\ge2), their exact number is

\[
 (r-2)(m-2).
\tag{6.10}
\]

For (r=1) the family is empty, so the count is zero.

For (d\ge2), the owner in (6.4) differs from (P_{d,j}) in the third
and fourth coordinates, so this is a literal two-pin owner, not a one-pin
completion.

### Theorem 6.1 (exact selected source-gap restoration tax)

Retain every original occurrence and the order of the diagonal path words,
allowing only insertions between them.  For every source gap

\[
 P_{d,j},q_{d,j}
 \qquad
 (2\le d\le r, 0\le j<m-1),
\]

also require a witness beginning at (P_{d,j}) for the common-lift child
target

\[
 b_{2r-d-2j,\,2j}
 =(h_{2r-d-2j};1,2j),
\tag{6.11}
\]

while retaining the middle witness (6.4).  Then exactly (E) insertions
are necessary and sufficient, where (E) is (6.7).

#### Proof

The next old letter is

\[
 q_{d,j}=(h_0;d-1,2j+1),
\]

which is not below (6.11), because its fourth coordinate is (2j+1).
Hence a witness for (6.11) starting at (P_{d,j}) must end in the open
gap before (q_{d,j}).  The portal has third coordinate zero, while
(6.11) has third coordinate one.  The gap must therefore contain at least
one new position which pins that coordinate and remains below (6.11).
The (E) source gaps are disjoint, proving necessity.

For sufficiency insert

\[
 e_0=(h_0;1,0)
\]

in every source gap.  Then

\[
 P_{d,j}\vee e_0=b_{2r-d-2j,2j},
\]

while (e_0\le P_{d,j}\vee q_{d,j}), because (d\ge2).  Thus

\[
 P_{d,j},e_0,q_{d,j}
\]

still has the middle maximum (6.4).  One insertion in every gap attains
the lower bound. \(\square\)

Since

\[
 E=(r-1)(\lceil r/2\rceil-1)=\frac12r^2+O(r),
\]

even this selected quadratic part of the two individually cheap
chronologies cannot be superposed immutably at subquadratic cost.
This obstruction is not the one-pin completion lemma: every middle owner
in (6.4) is already multipin.  The cost is caused by literal child-target
contamination in disjoint physical gaps.

---

## 7. Exact proved/conditional boundary

### Proved

1. The alternating snake, every meet identity, the row-start parity
   correction, the exact two parity-dependent lengths in (2.9), the
   \(r(r-2)\) genuine multipin count, and the occurrence/distinct-owner
   two-sided carrier counts (2.10)--(2.10a).

2. The one-word aligned-middle bound (2.11).

3. The half-upper block atlases, every literal interval, exact target
   counts (3.5), (3.12), and exact length (3.13).

4. The unrestricted packet lower bound (W_r+r), including the nonzero
   lower-target count and the integral remainder (5r-1).

5. The arbitrary-multipin immutable-matching obstruction (5.9), with the
   floor (k_r=\lfloor(r-1)/8\rfloor), exact (\Gamma_r), and coefficient
   (173/13824).

6. The diagonal path forest, exact component and edge counts, two-sided
   portal count, and exact insertion tax for the selected source-gap
   common-lift targets.  Restoring the full old common-lift system has at
   least this cost; sufficiency for every old child witness is not claimed.

### Not proved

1. A word of length (W_r+o(r^2)) covering **all** of
   (\mathcal A_r\cup\mathcal B_r).

2. Simultaneous service of the lower packet halves and the missing upper
   caps (3.14) inside either near-width atlas.

3. A dynamic hybrid which keeps the common-lift child service and the
   multipin middle paths without retaining either old chronology.

4. Any implication from these local results to the sharp constant-one
   theorem.

The precise frontier is therefore no longer a middle pin or static Hall
problem.  A positive-density, two-sided multipin middle carrier system
exists with only linear excess, and it covers a cubic half-upper family.
The remaining gate is **depth-compatible hybridization**: lower-half and
upper-cap witnesses must traverse the same carrier surface without paying
the quadratic immutable-gap tax of Theorem 6.1.

### Audit

The meet-carrier construction and row parity were independently derived
in a separate proof audit.  The present proof then rechecked every seam:
high-(v) turns, low-(v) repeated turns, odd row starts, both word
endpoints, and the effect of zeroing only the even carrier's third
coordinate.  A second independent construction audit derived the diagonal
path forest and its contamination tax.  The lower-bound audit recomputed
the packet rank polynomial and the exact division

\[
 2r^3+2r^2+r-1
 =(r-1)(2r^2+4r)+(5r-1).
\]

No unproved lemma is used in any boxed assertion above.
