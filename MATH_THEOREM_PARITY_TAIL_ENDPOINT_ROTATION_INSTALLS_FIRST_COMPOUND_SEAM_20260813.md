# A parity-tail endpoint rotation installs the first compound seam and preserves upper support

**Date:** 2026-08-13  
**Status:** claimed unconditional owner/immediate-lower relative trade,
with an explicit all-`m` MSW row certificate, protected-portal separation,
and old-upper-support preservation.  Root-local exact replay passes through
`m=101`; independent hostile audit is pending.  The trade uses `Theta(m)`
colours.  A positive-resident chronology is still a separate gate.

## 1. The first-aligned host and endpoint-rotation language

Let `m>=10`, `n=2m+1`, and let `F_m` be the complete offset-zero
first-aligned MSW packet factor.  Thus every rank-`m` facet `L` has one
old coloured edge

\[
                         e_0(L)=\{P_L,V_L\}                \tag{1.1}
\]

between two rank-`m+1` owners.  If `W` is another owner containing `L`,
the endpoint rotation

\[
                         \{P_L,V_L\}\longmapsto\{P_L,W\}  \tag{1.2}
\]

preserves the colour `L` and changes the moving owner from `V_L` to `W`.

Use the PBBS owners `C=C_4` and `U=U_5`, and put

\[
                         L_0=C\cap U.                      \tag{1.3}
\]

Let `A,B` be the two old endpoints of `e_0(L_0)`, assigned so that the
paths below end at `A` and `B` respectively.

## 2. The two open paths

For a set `X`, write `X-x+y=(X\setminus\{x\})\cup\{y\}`.

### The fixed path

Define

\[
\begin{aligned}
P_0={}&C,\\
P_1={}&P_0-(2m-4)+3,\\
P_2={}&P_1-5+2,\\
P_3={}&P_2-(2m)+(2m-4),\\
P_4={}&P_3-3+(2m-3),\\
P_5={}&P_4-2+(2m)=A.                                  \tag{2.1}
\end{aligned}
\]

### The parity-tail ladder

Put

\[
 b_m=\begin{cases}11,&m\text{ even},\\13,&m\text{ odd},\end{cases}
 \qquad t_m=\left\lfloor{m-4\over2}\right\rfloor.        \tag{2.2}
\]

Starting at `Q_0=U`, make the exchanges

\[
 -(2m-2)+b_m,\qquad -10+(b_m+4),                         \tag{2.3}
\]

then, for `0<=j<t_m-3`,

\[
                         -(b_m+4j)+(b_m+4j+8),            \tag{2.4}
\]

and finally

\[
                         -(b_m+4(t_m-3))+(2m-2).          \tag{2.5}
\]

Call the resulting owners `Q_0,...,Q_(t_m)`.  Then

\[
                         Q_{t_m}=B.                       \tag{2.6}
\]

The path has `t_m` edges.  It is a ladder rather than a bounded gadget;
its middle exchanges move a defect two pair-blocks at a time through the
alternating tail.

## 3. Explicit MSW root certificates

We record the root which contains the old edge at each path step.  For a
Dyck root with its displayed first-aligned `1100` block, the complete
packet replaces its two negative rows by the usual positive inverse pair.

### Lemma 3.1 (fixed-path rows)

The five old edges of `(2.1)` lie respectively in positive packet rows
coming from

\[
\begin{aligned}
&101110011100(10)^{m-7}00,\\
&101111011100(10)^{m-8}0000,\\
&101100111100(10)^{m-8}0010,\\
&111001001100(10)^{m-6},\\
&111111000001(01)^{m-8}0010.                         \tag{3.1}
\end{aligned}
\]

The aligned block begins at bit `8` in the first four roots and bit `4`
in the last.

### Lemma 3.2 (tail-ladder rows)

The first two old edges of `(2.3)` lie in positive packet rows from

\[
                         101111000110(10)^{m-7}00        \tag{3.2}
\]

and, according to parity,

\[
 \begin{cases}
 10111100010110(10)^{m-8}00,&m\text{ even},\\
 1011110001100110(10)^{m-9}00,&m\text{ odd}.
 \end{cases}                                            \tag{3.3}
\]

For `2<=r<t_m`, the `r`-th subsequent old edge lies in the positive row
from

\[
 101111000111(01)^{,2r-4+(m\bmod2)}000110
 (10)^{,m-2r-6-(m\bmod2)}00.                           \tag{3.4}
\]

Every aligned block in `(3.2)-(3.4)` begins at bit `4`.

### Lemma 3.3 (seam row)

The old seam edge `e_0(L_0)=\{A,B\}` lies in a positive row from

\[
                         101111000111(01)^{m-8}0000,      \tag{3.5}
\]

again with aligned block at bit `4`.

#### Proof of Lemmas 3.1--3.3

All displayed roots are Dyck words.  Use the standard MSW concatenation
and shell identities

\[
 \rho(XY)=\rho(X)\Vert(|X|+\rho(Y)),                    \tag{3.6}
\]

\[
 \rho(1x0)=
 (|x|+2,\ |x|+2-\rho(\mu x),\ 1),                     \tag{3.7}
\]

together with

\[
 \rho(W_{j+2})=
 (2M_j+4,\ 2,\ \rho(W_j)+2,\ 2M_j+3,\ 1).             \tag{3.8}
\]

The suffix `(10)^s` in `(3.1)-(3.3)` contributes consecutive translated
flip pairs by `(3.6)`.  In `(3.4)`, increasing `r` by one adds two shells
to the `(01)` block and removes two `(10)` leaves.  Equation `(3.8)` moves
the distinguished owner exchange from

\[
                         -(b_m+4r-8)+(b_m+4r)             \tag{3.9}
\]

to the next such exchange, while keeping every common even tail label.
The final shell specializes `(3.9)` to `(2.5)`.  Reading the corresponding
consecutive owner windows gives exactly `(2.1)` and `(2.3)-(2.5)`.

For `(3.5)`, the same shell recursion gives the two extras over `L_0`
as the endpoints reached by the two paths.  Thus the old edge is
`\{A,B\}`.  This proves all three lemmas. \(\square\)

## 4. The exact relative seam trade

At each path step `X->Y`, retain the stationary endpoint of the old edge
certified in Section 3 and rotate `X` to `Y`.  At `L_0`, replace

\[
                         \{A,B\}\longmapsto\{C,U\}.       \tag{4.1}
\]

### Theorem 4.1 (parity-tail seam installation)

For every `m>=10`, the replacements above

1. use exactly
   \[
        6+t_m                                             \tag{4.2}
   \]
   distinct facet colours;
2. preserve every rank-`m` facet exactly once;
3. preserve degree two at every rank-`m+1` owner; and
4. install the compound seam `C_4-U_5`.

#### Proof

Distinctness of the path colours follows from the successive exchanged
label pairs and the exceptional markers in `(2.1)-(2.5)`; none equals
`L_0`.  Each replacement preserves its own colour.

The first open path has moving-owner defect `-C+A`; the second has
`-U+B`; and `(4.1)` has `-A-B+C+U`.  Their sum is zero.  Stationary
endpoints cancel termwise.  Hence every owner degree is preserved. \(\square\)

## 5. The repair circuit and protected portal rows

There is also a fixed six-edge endpoint-rotation circuit.  Put

\[
 E_m=\{16,18,\ldots,2m-4\}                             \tag{5.1}
\]

and lift the base cycle

\[
\begin{aligned}
&2689(10)(12)(14)(15)(16)(17),\\
&26789(10)(12)(14)(15)(16),\\
&026789(12)(14)(15)(16),\\
&012679(12)(14)(15)(16),\\
&01269(10)(12)(14)(15)(16),\\
&0269(10)(12)(14)(15)(16)(17),\\
&2689(10)(12)(14)(15)(16)(17)                         \tag{5.2}
\end{aligned}
\]

by adjoining `E_m` and replacing `15,16,17,18` by
`2m-3,2m-2,2m-1,2m`.  The six old edges occur in the rows with roots

\[
\begin{aligned}
110111010001(01)^{m-8}0010,&\quad
110111000011(01)^{m-8}0010,\\
111111000001(01)^{m-8}0010,&\quad
111001110001(01)^{m-8}0010,\\
111001011001(01)^{m-8}0010,&\quad
110111011001(01)^{m-8}0000.                          \tag{5.3}
\end{aligned}
\]

The second and third are positive first-aligned rows; the others are
unchanged canonical rows.  The same recursion `(3.6)-(3.8)` proves these
identities.  The six rotations form a closed moving-owner circuit, so
they preserve all middle and lower rows independently of Theorem 4.1.
Their six colours are pairwise distinct and are disjoint from the path and
seam colours, as is immediate from the exceptional-marker profiles in
`(2.1)-(2.5)` and `(5.2)`.

### Theorem 5.1 (selected internal portals are untouched)

Let the deadline `d` satisfy `m>=3d+2`.  None of the colours in Theorem
4.1 or the six-edge circuit lies on a selected positive portal row of
`MATH_THEOREM_PBBS_INTERNAL_HEIGHT_SPINE_TARGETS_HAVE_PAIRWISE_CONFORMAL_MSW_PORTALS_20260813.md`.

#### Proof

Every selected portal row is a positive row of a packet whose negative
roots have their first aligned `1100/1010` block at bit `0`:

\[
                         1100z_{A,q},\qquad1010z_{A,q}.  \tag{5.4}
\]

By inspection of `(3.1)-(3.5)` and `(5.3)`, every positive host row used
by the present trade comes from a packet whose first aligned block is at
bit `4`, `8`, or `12`; the other repair hosts are unchanged canonical
rows.  Hence no changed host row is a selected portal row.  Since `F_m`
is an exact rank-`m` window factor, distinct rows have disjoint facet
decks.  Therefore no changed colour lies on a selected portal row.
\(\square\)

## 6. Explicit upper-support backups

For every changed colour `L`, the immediate-upper current changes by

\[
 \mathbf e_{P_L\cup W_L}-\mathbf e_{P_L\cup V_L}.       \tag{6.1}
\]

The two open paths alone have one singleton-load loss: it is the old upper
value of the last fixed-path edge, and it is exactly the new upper value
of the first edge in the repair circuit `(5.2)`.  Every remaining negative
term of the combined current has a second occurrence in an untouched row.
Here is a complete root table.

For the first three fixed-path steps use, respectively,

\[
\begin{aligned}
&101110011011(01)^{m-8}0000,\\
&101111111100(10)^{m-9}000000,\\
&111100111100(10)^{m-8}0000.                         \tag{6.2}
\end{aligned}
\]

The first is an unchanged row; the other two use their first aligned block
at bit `8`.

For the tail-ladder step `0` use

\[
                         1011110101101100(10)^{m-10}0000, \tag{6.3}
\]

with aligned block at bit `12`.  For step `1`, use

\[
 \begin{cases}
 1011110100011100(10)^{m-10}1000,&m\text{ even},\\
 1011110001010110(10)^{m-9}00,&m\text{ odd},
 \end{cases}                                             \tag{6.4}
\]

with aligned block at bit `12` or `4` respectively.  For a tail step
`2<=r<t_m`, put

\[
 a_r=2r-4+(m\bmod2),\qquad c_r=m-2r-6-(m\bmod2).         \tag{6.5}
\]

Its backup root is

\[
 \begin{cases}
 101111000110010110(10)^{c_r}00,&a_r=0,\\
 101111000111(01)^{a_r-1}00010110(10)^{c_r}00,&a_r>0,
 \end{cases}                                             \tag{6.6}
\]

with aligned block at bit `4`.

For repair steps `0,1,2,4,5`, use

\[
\begin{aligned}
&111111010001(01)^{m-8}0000,\\
&11011100001111(01)^{m-9}0000,\\
&111110001001(01)^{m-8}0010,\\
&111100100101(01)^{m-8}0010,\\
&110011011001(01)^{m-8}0100.                         \tag{6.7}
\end{aligned}
\]

Rows `1` and `5` in this list use aligned blocks at bits `4` and `0`; the
other three are unchanged canonical rows.  Finally the old seam upper
value has a backup in the positive row from

\[
                         101111000111(01)^{m-9}000100,    \tag{6.8}
\]

with aligned block at bit `4`.

### Lemma 6.1 (literal backup identity)

For each source step named in `(6.2)-(6.8)`, the indicated row has a
length-`m+2` cyclic window equal to the old upper value of that step.
None of these backup rows is a changed host row.

#### Proof

Apply `(3.6)-(3.8)`.  The fixed roots `(6.2)`, `(6.7)`, and `(6.8)` differ
from their source roots only in the displayed bounded exceptional block,
and the common translated tail supplies the same `m+2` window.  For
`(6.3)-(6.6)`, increasing `r` adds the same two shells on both source and
backup sides; `(3.8)` translates the common window by two and adds the
same new terminal labels.  The base cases `r=0,1,2` are the first three
displayed formulas, so induction proves every tail rung.

The backup roots are pairwise distinct from all roots `(3.1)-(3.5)` and
`(5.3)`.  Their first-aligned positions, where present, also identify
different packet pairs.  The remaining roots index unchanged canonical
rows.  Thus their rows are untouched. \(\square\)

### Theorem 6.2 (old upper support is preserved)

Apply the seam trade and the six-edge repair circuit simultaneously.  If
`mu_0^+` and `mu_1^+` are the old and new immediate-upper load vectors,
then

\[
                 \operatorname{supp}\mu_0^+
                 \subseteq\operatorname{supp}\mu_1^+.  \tag{6.9}
\]

#### Proof

After cancelling equal positive and negative terms in `(6.1)`, the
negative support is contained in the first three fixed-path steps, all
tail-ladder steps, repair steps `0,1,2,4,5`, and the seam.  The last
fixed-path loss is created by repair step `0`; the old upper of fixed step
`3` equals the new upper of fixed step `2`, and the old upper of repair
step `3` equals the new upper of fixed step `3`.  Lemma 6.1 leaves an untouched occurrence
of every remaining negative value.  Therefore no old positive load falls
to zero. \(\square\)

## 7. Scope and verification

The theorem closes the literal all-`m` owner/lower/relative-upper and
protected-portal incidence recurrence for the first compound seam.  The
combined trade uses

\[
                         t_m+12=\Theta(m)                \tag{7.1}
\]

distinct colours.  Its price is therefore linear
in `m`, so independent repetition at every low-spine height would be too
large without sharing.  More importantly, it does not yet order the
changed row fragments into a positive-resident chronology.

The root-local verifier

* `scratch/verify_symbolic_endpoint_ladder_roots_20260813.py`

evaluates only the displayed roots, never the Catalan-size factor.  It
checks Dyck validity, literal old-edge membership, distinct colours, owner
balance, selected-portal colour avoidance, every backup occurrence, and
upper-support monotonicity.  Exact H100 replay passed
`m=10,11,12,13,14,17,20,31,64,101`; this audits the formulas but is not
used in place of the symbolic recurrences above.
