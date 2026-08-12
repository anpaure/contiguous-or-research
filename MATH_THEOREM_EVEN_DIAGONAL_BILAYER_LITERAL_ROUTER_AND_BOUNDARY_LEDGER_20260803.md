# Even diagonal rows: bilayer occurrence router, boundary detachment, and socket ledger

**Date:** 2026-08-03  
**Status:** unconditional fixed-row theorem and single-role capacity obstruction.
No computation is used.  The theorem does not construct the required even
row, compatible post-compensation sockets, upper-complete opening, or an
all-dimensional OR word.

## 0. Result

Put

\[
 K=2r,
 \qquad S=[K]\setminus\{z\},
 \qquad W={2r\choose r},
 \qquad M={W\over2}={2r-1\choose r},
 \qquad C={W\over r+1}=\operatorname {Cat}_r.
\tag{0.1}
\]

The rank-\(r\) owner layer has two bilayer shores

\[
 {\cal A}={S\choose r},
 \qquad
 {\cal B}=\{z\}+{S\choose r-1},
 \qquad |{\cal A}|=|{\cal B}|=M.
\tag{0.2}
\]

The equality in (0.2) is a proved binomial identity; it is not an
assumption about the lower ports.  The two immediate-lower target shores
have the unequal sizes

\[
 |{\cal L}_0|=\left|{S\choose r-1}\right|=M,
 \qquad
 |{\cal L}_z|=\left|\{z\}+{S\choose r-2}\right|=M-C.
\tag{0.3}
\]

Assume \(2\le d<W\).  Let a cyclic literal diagonal row have nonempty
source letters \(A_i\),
owner occurrences

\[
 T_i=\bigcup_{j=i}^{i+d}A_j\in{[K]\choose r},
\tag{0.4}
\]

and lower-port occurrences

\[
 P_i=\bigcup_{j=i+1}^{i+d}A_j
     =T_i\cap T_{i+1}\in{[K]\choose r-1}.
\tag{0.5}
\]

Assume the \(T_i\) enumerate the complete middle layer once.  The \(P_i\)
need not have distinct values.  Then the occurrence graph

\[
 p_i o_i,\qquad p_i o_{i+1}
\tag{0.6}
\]

is still one balanced alternating \(2\)-factor on \(W+W\) **occurrences**.
Its two edges at \(p_i\) have the literal extensions

\[
 P_i\cup A_i=T_i,
 \qquad
 P_i\cup A_{i+d+1}=T_{i+1}.
\tag{0.7}
\]

Thus the odd diagonal router survives in even dimension after one replaces
"one port value each" by "one real occurrence per lower target, plus
occurrence-labelled dummy ports."  If the lower q1 row is surjective, the
number of dummies is exactly

\[
 W-{2r\choose r-1}=C.
\tag{0.8}
\]

Both explicit routing phases are pairwise resource-disjoint, and the union
of the phases has normalized overload zero.  No abstract suffix-expansion
theorem is needed before the terminal socket.

The bilayer accounting is exact.  If the cyclic top trace

\[
 \epsilon_i=1_{\{z\in T_i\}}
\tag{0.9}
\]

has \(h\) one-runs, then the lower-port occurrence counts and lower-target
counts are as follows; the last column is the exact dummy count when the
lower q1 row is surjective:

\[
\begin{array}{c|ccc}
 &\text{occurrences}&\text{targets}&\text{dummies}\ 
\hline
 z\notin P&M+h&M&h\\
 z\in P&M-h&M-C&C-h.
\end{array}
\tag{0.10}
\]

The immediate-upper turn occurrences \(U_i=T_i\cup T_{i+1}\) have the
complementary ledger; here the last column is the exact dummy count when
the upper q1 row is surjective:

\[
\begin{array}{c|ccc}
 &\text{occurrences}&\text{targets}&\text{dummies}\ 
\hline
 z\notin U&M-h&M-C&C-h\\
 z\in U&M+h&M&h.
\end{array}
\tag{0.11}
\]

Consequently either lower or upper q1 surjectivity already forces

\[
                         1\le h\le C.
\tag{0.12}
\]

The vectors of lower and upper dummy masses are antidiagonal:

\[
             (h,C-h),\qquad(C-h,h).
\tag{0.13}
\]

This equality is only a type/count identity.  It does not by itself pair
the two physical dummy banks or create terminal capacity.

Linearizing the cyclic source splits the closing lower port into two
distinct boundary occurrences.  The exact physical incidence object is
therefore an alternating path with \(W\) owners and \(W+1\) ports, not an
equal-shore cycle.  Either boundary-deleted phase is nevertheless an
explicit full \(W\)-port router.  This boundary detachment forces at least
\(C+1\) unused rank-\((r-1)\) cells in any injective lower compiler.

For the capacity statements, now specialize \(d\) to the lower-bound
deadline \(d(K)\).  Let

\[
 \Lambda=\sum_{s=1}^{r-1}{2r\choose s},
 \qquad
 \tau_d={d(d+1)\over2},
 \qquad
 \sigma=dW+\tau_d-\Lambda.
\tag{0.14}
\]

At exact length \(B(K)=W+d\), any linearized diagonal face that admits an
injective exact strict-lower compiler necessarily satisfies

\[
                         \boxed{\sigma\ge C+1}.
\tag{0.15}
\]

If the q1 row is the designated immediate-upper witness bank and the only
single-role terminal resources are the distinct, no-alias bank of unused
short cells and surplus immediate-upper cells, then a safe linear opening
supplies at most

\[
                         \sigma+C-1
\tag{0.16}
\]

distinct terminal units.  Hence its full \(W\)-port terminal deficiency is
at least

\[
                         \boxed{(W-\sigma-C+1)_+}.
\tag{0.17}
\]

The \(C+1\) lower-port duplicates in (0.15) are already part of \(\sigma\)
and may not be added to (0.16) a second time.  At length \(B+1\), on the
face retaining the complete width-\((d+1)\) diagonal owner band, after
reserving its \(W\) owner cells the analogous no-alias upper bound is

\[
                         \sigma+d+1+C,
\tag{0.18}
\]

and the corresponding deficiency is at least

\[
                         (W-\sigma-d-1-C)_+.
\tag{0.19}
\]

Equations (0.15)--(0.19) are scoped exact-compiler, single-role cuts.  A dual-role ticket,
a remote compatible socket bank, or a different common-cap linkage may
evade them.

## 1. Bilayer sizes and transition ledger

The middle shores in (0.2) have the same size because

\[
 {2r-1\choose r}={2r-1\choose r-1}={1\over2}{2r\choose r}.
\tag{1.1}
\]

The lower and upper target counts follow from

\[
 {2r-1\choose r-2}
 ={r-1\over r+1}{2r-1\choose r-1}=M-C,
\tag{1.2}
\]

and complementation in \(S\).

Because the owner row visits every middle set, the binary word
\(\epsilon\) has \(M\) zeros and \(M\) ones.  A cyclic binary word with
\(h\) one-runs has \(h\) transitions of type \(0\to1\), \(h\) of type
\(1\to0\), and therefore

\[
 \#AA=M-h,
 \qquad
 \#BB=M-h,
 \qquad
 \#\text{cross}=2h.
\tag{1.3}
\]

Here \(A\) means an owner omitting \(z\), and \(B\) means an owner
containing \(z\).  For one Johnson edge the lower and upper types are

\[
\begin{array}{c|cc}
 \text{edge type}&T_i\cap T_{i+1}&T_i\cup T_{i+1}\\
\hline
 AA&z\text{-free}&z\text{-free}\\
 BB&z\text{-containing}&z\text{-containing}\\
 AB,BA&z\text{-free}&z\text{-containing}.
\end{array}
\tag{1.4}
\]

Equations (0.10)--(0.11) now follow by adding (1.3) and subtracting
the target counts (0.3) and their upper analogues.  Nonnegativity of the
\(z\)-containing lower surplus, or equivalently of the \(z\)-free upper
surplus, gives (0.12).

The incidence degrees also balance exactly, despite the unequal lower
value shores.  The \(AA\) ports contribute \(2(M-h)\) incidences to
\({\cal A}\); the cross ports contribute \(2h\) incidences to each owner
shore; and the \(BB\) ports contribute \(2(M-h)\) incidences to
\({\cal B}\).  Each owner shore therefore receives exactly \(2M\)
incidences.

## 2. Cyclic occurrence router

Give every interval its occurrence address.  Form the graph \(F\) on port
occurrences \(p_i\) and owner occurrences \(o_i\), with edges (0.6).
Every port has degree two, every owner \(o_i\) is incident with
\(p_i,p_{i-1}\), and the addressed graph is

\[
 o_0,p_0,o_1,p_1,\ldots,o_{W-1},p_{W-1},o_0.
\tag{2.1}
\]

Repeated values among the \(P_i\) do not alter (2.1).  Under lower q1
surjectivity, select one occurrence of every rank-\((r-1)\) target as real
and label every remaining occurrence dummy.  There are exactly \(C\)
dummies by (0.8).  The real-plus-dummy occurrence shore has size \(W\), so
it is the correct shore for the balanced router; the set of distinct port
values is not.

The two literal routes at \(p_i\) are

\[
 R_i^-:p_i\longrightarrow a_i\longrightarrow\tau_i,
 \qquad
 R_i^+:p_i\longrightarrow a_{i+d+1}\longrightarrow\tau_{i+1},
\tag{2.2}
\]

where \(\tau_i\) is a compatible unused unit socket for owner type \(T_i\).
The sockets \(\tau_i\) are assumed pairwise distinct and disjoint, as
physical resources, from the displayed port and source occurrences.
The semantic identities are exactly (0.7).  The minus phase uses the
distinct triples \((p_i,a_i,\tau_i)\), and the plus phase uses the distinct
triples \((p_i,a_{i+d+1},\tau_{i+1})\).  Thus either phase is a disjoint
full linkage.

If both options are retained, every port, source occurrence, and terminal
socket has raw multiplicity two.  Uniform weight \(1/2\) has load one on
every unit resource.  This proves zero overload in the displayed ledger.
As usual, hidden guards and state resources must either be private or be
included in the ledger.

Nothing in this proof exports \(\tau_i\).  On the native-owner-only face,
if the owner capacities \(o_i\) are reserved by middle ownership and no
remote terminal is admitted, deleting them leaves suffix rank zero.  The
exact missing interface is one compatible unused socket per owner, or an
equivalent full-rank typed terminal matching.

## 3. Literal linear boundary detachment

Write the physical linearization as

\[
 \widehat A_j=A_{j\bmod W},
 \qquad 0\le j<W+d.
\tag{3.1}
\]

Its \(W\) owner cells are

\[
 o_i=[i,i+d],
 \qquad 0\le i<W,
\tag{3.2}
\]

and its \(W+1\) width-\(d\) port cells are

\[
 p_j=[j,j+d-1],
 \qquad 0\le j\le W.
\tag{3.3}
\]

Their values satisfy

\[
 \operatorname{OR}(p_{i+1})=P_i\quad(0\le i<W-1),
 \qquad
 \operatorname{OR}(p_0)=\operatorname{OR}(p_W)=P_{W-1}.
\tag{3.4}
\]

Thus the cyclic closing port is detached into two distinct physical
boundary occurrences.  The physical incidence graph is the alternating
path

\[
 p_0,o_0,p_1,o_1,\ldots,p_{W-1},o_{W-1},p_W.
\tag{3.5}
\]

There are still two explicit full routing phases:

\[
 \begin{aligned}
 {\cal R}^{\rightarrow}
   &=\{p_i\xrightarrow{\widehat A_{i+d}}o_i:0\le i<W\},\\
 {\cal R}^{\leftarrow}
   &=\{p_{i+1}\xrightarrow{\widehat A_i}o_i:0\le i<W\}.
 \end{aligned}
\tag{3.6}
\]

The first phase omits \(p_W\), the second omits \(p_0\), and each routes
\(W\) physical ports to all \(W\) owners with pairwise distinct
source-letter occurrences.  Logically, the closing cyclic port has the two-entry occurrence
menu \(\{p_0,p_W\}\).  Giving its two routes weight \(1/2\), and doing the
same at every internal logical port, gives one unit from every logical
port, one unit into every owner socket, and load at most one on every
physical port and source occurrence.  Hence the boundary detachment has
zero overload as well.

For \(d=1\), port cells and source-letter cells alias.  The set identities
and the two integral phases remain valid, but the separated port/letter
overload ledger is not asserted without coalescing those capacities.

## 4. Forced compiler slack and the safe-opening ledger

At length \(W+d\), the number of interval cells of widths at most \(d\) is

\[
 \sum_{\ell=1}^d(W+d-\ell+1)=dW+\tau_d.
\tag{4.1}
\]

Every longer interval contains one of the width-\((d+1)\) owner cells, so
its union has rank at least \(r\).  Hence every strict-lower witness lies in
the pool (4.1).

If an injective exact strict-lower compiler exists, it uses \(\Lambda\) of
them and leaves
exactly \(\sigma\) unused.  All \(W+1\) cells in (3.3) have rank \(r-1\),
but they realize only the \(W-C\) possible rank-\((r-1)\) targets.  A cell
of rank \(r-1\) can serve no different lower target.  Therefore at least

\[
                       (W+1)-(W-C)=C+1
\tag{4.2}
\]

of these physical cells are unused by every injective compiler.  This
proves (0.15).

The width-\((d+2)\) upper cells of the linear word number \(W-1\): they are
the cyclic upper turns except for the closing turn.  If the cyclic upper
row is surjective and the omitted closing occurrence has another provider,
the opening is **upper-safe** and exactly

\[
                    (W-1)-{2r\choose r+1}=C-1
\tag{4.3}
\]

of these upper cells remain after reserving one occurrence per upper
target.  They are disjoint in width from the short pool (4.1).  Hence the
single-role free bank has size at most \(\sigma+C-1\), proving
(0.16)--(0.17).

The \(C+1\) lower duplicates in (4.2) are a subbank of the \(\sigma\)
unused short cells.  Adding them to \(\sigma\) would count the same physical
addresses twice.

At length \(W+d+1\), on the face retaining the complete width-\((d+1)\)
diagonal owner band, the pool through width \(d+1\) has size

\[
                   (d+1)W+\tau_{d+1}.
\tag{4.4}
\]

After reserving \(\Lambda\) strict-lower cells and \(W\) central owners,
at most \(\sigma+d+1\) units remain.  There are now \(W\) width-\((d+2)\)
upper cells, with at most \(C\) surplus after upper coverage.  This proves
(0.18)--(0.19).

More generally, for fixed additive charge \(c\ge1\), put \(e=d+c\).  Assume
the word retains a complete width-\((d+1)\) diagonal owner band and, for
every \(1\le j<c\), a complete rank-\((r+j)\) diagonal band in the counted
width pool.  After reserving all strict-lower targets, the \(W\) central
owners, and one witness for every target in those admitted upper bands, the
single-role free capacity is at most the following quantity.  When \(c=1\),
the final \(C\) term additionally grants the complete cyclic q1 surplus as
a distinct no-alias bank outside the counted pool:

\[
 \boxed{
 F_c\le
 \sigma+(\tau_{d+c}-\tau_d)
 +\sum_{j=1}^{c-1}
       \left(W-{2r\choose r+j}\right)
 +\mathbf 1_{\{c=1\}}C.}
\tag{4.5}
\]

For fixed \(c\), every displayed term apart from \(\sigma\) is \(o(W)\):

\[
 { {2r\choose r+j}\over W}
 =\prod_{\ell=1}^j{r-\ell+1\over r+\ell},
 \qquad
 W-{2r\choose r+j}=O_j(W/r),
\tag{4.6}
\]

and \(\tau_{d+c}-\tau_d=O_c(d)\).

## 5. Type-refined opening and terminal cut

Let the closing edge have type \(AA\), \(BB\), or cross.  The duplicated
boundary lower port in (3.4) contains \(z\) exactly in the \(BB\) case.
Thus the following vector is a componentwise lower bound on the unused
lower-port cells in the linear word (and is exact when each lower q1 target
is assigned inside this port row):

\[
\begin{array}{c|cc}
 \text{closing edge}&z\text{-free}&z\text{-containing}\\
\hline
 AA&h+1&C-h\\
 BB&h&C-h+1\\
 AB,BA&h+1&C-h.
\end{array}
\tag{5.1}
\]

If the omitted closing upper occurrence is redundant, the linear upper
surplus vector is

\[
\begin{array}{c|cc}
 \text{closing edge}&z\text{-free}&z\text{-containing}\\
\hline
 AA&C-h-1&h\\
 BB&C-h&h-1\\
 AB,BA&C-h&h-1.
\end{array}
\tag{5.2}
\]

In particular, an \(AA\) safe opening needs \(C-h\ge1\), while a \(BB\)
or cross safe opening needs \(h\ge1\).  These inequalities are necessary,
not sufficient: the omitted **value** must actually have another provider.

There is also a conditional typed terminal cut.  A \({\cal B}\)-owner
contains \(z\), so an immediate-upper occurrence containing that owner must
belong to the \(z\)-containing upper stratum.  Let

\[
 h'=h-\mathbf 1_{\{\text{the safe opening deletes a }z
                              \text{-containing upper dummy}\}},
\tag{5.3}
\]

and let \(\sigma_B\) be the number of unused short/common-cap units that
the fixed terminal semantics actually admit for \({\cal B}\)-owner tickets,
counted on physical resources disjoint from the surplus immediate-upper
cells.
On the face using only these units and surplus immediate-upper cells, the
\({\cal B}\) terminal cut has capacity at most \(h'+\sigma_B\).  Therefore

\[
                   \boxed{\delta_B\ge(M-h'-\sigma_B)_+.}
\tag{5.4}
\]

This does not identify \(\sigma_B\) with the number of cells whose values
contain \(z\); the common-cap semantics must prove compatibility.  Equation
(5.4) is precisely why a total scalar surplus is not a typed router theorem.

## 6. Equivariant specialization and calibrations

In the equivariant \((c,t)\) normal form, put \(n=2r-1\) and
\(N=W/n\).  If the quotient top word \(t\) has \(h_t\) one-runs, the
physical owner trace has

\[
                         h=n h_t.
\tag{6.1}
\]

The raw bilayer capacity (0.12) becomes

\[
                         h_t\le {N\over r+1}.
\tag{6.2}
\]

This recovers the ordinary run-count bound in the equivariant catalogue.
Exceptional short necklace orbits may sharpen (6.2); that is an additional
orbit theorem, not part of the literal occurrence router.

For \(K=14\),

\[
 W=3432,\quad r=7,\quad C=429,\quad d=2,\quad
 \Lambda=6475,\quad \sigma=392.
\tag{6.3}
\]

Since \(392<430=C+1\), (0.15) proves that no exact-length word on this
single cyclic q1-surjective flat diagonal face can have an injective lower
compiler.  This is a face obstruction, not a contradiction to the known
nonflat/noncyclic optimum.

For \(K=16\),

\[
 W=12870,\quad M=6435,\quad C=1430,\quad d=3,\quad
 \Lambda=26332,\quad \sigma=12284.
\tag{6.4}
\]

The boundary condition (0.15) passes, and the total single-role count
\(\sigma+C-1=13713\) exceeds \(W\).  Hence there is no total scalar socket
cut on this face.  The unresolved statement is genuinely typed and
physical: one must produce compatible post-compensation sockets, or prove a
capacity-faithful common-cap linkage.  The bilayer count alone does neither.

## 7. Exact frontier

The even analogue closes the following implication:

\[
\boxed{
\begin{array}{c}
\text{cyclic q1-surjective literal even diagonal row}\\
+\ \text{one real occurrence per lower target and }C\text{ dummies}\\
+\ \text{one compatible unused socket per owner occurrence}
\end{array}
\Longrightarrow
\text{exact zero-overload }h=2\text{ literal router}.}
\tag{7.1}
\]

The row itself, the safe upper opening, and the terminal socket bank remain
separate existence problems.  In particular, equality of the two middle
owner shores does not erase the unequal q1 value shores, the forced dummy
ports, the physical boundary split, or the terminal type cut.
