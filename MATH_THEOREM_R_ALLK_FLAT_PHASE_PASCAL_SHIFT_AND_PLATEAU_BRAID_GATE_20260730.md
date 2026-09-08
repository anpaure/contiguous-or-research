# Flat-phase Pascal transport and the exact plateau-braid gate

Date: 2026-07-30  
Lane: R  
Status: pure mathematics.  The protected flat-shift identity, the
order-`a` Pascal identity, the phase-credit criterion, and the shifted Hall
tower theorem are proved.  The existence of a phase-balanced protected braid
is isolated as an explicit unproved hypothesis.  No all-`k` equality claim is
made.

## 0. Result and proof boundary

The exact content is as follows.

1. On a locally geodesic rank-`r` block, moving an inherited exact-envelope
   compiler block
   past `t` generalized flats changes its local horizon from `q` to `q-t`.
   Every surviving width-`ell` provider acquires exactly `t` consecutive
   event coordinates.  Its rank rises by exactly `t`; its width and
   top/no-top tag do not change.
2. This statement holds simultaneously for every Pascal facet
   
   \[
       P^{(a)}_i=Z_a\cup\bigcap_{v=0}^{a}V_{i+v},
       \qquad |Z_a|=a,
   \]
   because a child depth-`q` maximal envelope is literally a parent
   depth-`q+a` maximal envelope with the fixed tag `Z_a` added.  Transport
   of an arbitrary chosen literal parent compiler additionally requires the
   facet-transparency identity in Proposition 3.2.
3. For a parent atlas already protected and flag-complete through depth `D`,
   the depth availability and residence needed by an order-`a` child piece
   placed at phase loss `f` are inherited exactly under the sharp universal
   phase-credit inequality
   
   \[
       \boxed{f+(D-d)\ge a.}
   \]
4. An exact Pascal Hall tower shifted upward by `t` has deficiency equal to
   the bottom `t` diagonals plus its explicitly deleted labels.  Carrier 3
   is the calibrated case
   
   \[
       519-497=19+1+2.
   \]
5. On a depth-drop odd-even step, an order-one intersection piece has one
   unit of inherited phase credit.  On a plateau it must be placed after a
   flat (or come from a depth-`d+1` parent); placing it after a flat repairs
   the residence unit but truncates the bottom compiler diagonal of that
   moved block.  Another phase-zero piece may compensate it.

What remains unproved is not a rank count.  A plateau-closing braid must
provide one common literal source `Q` and a full-signature matching for the
uncompensated moved-block bottom diagonal, width truncations, and cut/seam
casualties, while
also replaying the upper seams, endpoints, and top singleton.  Section 7
states this hypothesis exactly and proves that it is sufficient.  Relative
to fixed protected interiors it is also the exact remaining lower-compiler
condition.  Its all-`k` existence is open.

## 1. Protected Johnson blocks and compiler cells

Let

\[
    V=(V_j)_{j\in I},\qquad V_j\in {\binom{\Omega}{r}},
\]

be a rank-`r` Johnson stream.  Thus, whenever both sides are defined,

\[
    V_{j+1}=V_j-\alpha_j+\beta_j.                 \tag{1.1}
\]

For integers `q>=0`, `ell>=1`, define the backward depth-`q` envelope and
the width-`ell` compiler cell

\[
\begin{aligned}
    E_q^V(p)&=\bigcap_{u=0}^{q}V_{p-u},\\
    U_q^V(p,\ell)&=\bigcup_{v=0}^{\ell-1}E_q^V(p+v).
                                                        \tag{1.2}
\end{aligned}
\]

The full dependency collar of this cell is

\[
    V_{p-q},V_{p-q+1},\ldots,V_{p+\ell-1}.       \tag{1.3}
\]

Call the cell **protected** if (1.3) is a geodesic Johnson path: every
subpath has Johnson distance equal to its length.  In particular, on this
collar no coordinate is toggled twice: the departures and arrivals are
separately distinct, no arrival is subsequently removed, and no departure
is reinserted.  This is the local hypothesis used below.  Residence together
with the protected all-depth tight-flag/no-return
condition is a sufficient source of such collars; residence by itself is
not being used to infer geodesicity.  Mere Johnson adjacency is not enough.

### Lemma 1.1 (exact event formula)

For every protected cell (1.2),

\[
    E_q^V(p)=V_p\setminus
       \{\beta_{p-q},\ldots,\beta_{p-1}\},       \tag{1.4}
\]

and

\[
    U_q^V(p,\ell)=E_q^V(p)\cup
       \{\beta_{p-q},\ldots,\beta_{p-q+\ell-2}\}.
                                                        \tag{1.5}
\]

In particular,

\[
    |E_q^V(p)|=r-q,
    \qquad |U_q^V(p,\ell)|=r-q+\ell-1.           \tag{1.6}
\]

#### Proof

The coordinate `beta_j` is absent before transition `j`, enters at that
transition, and, by geodesicity of the whole dependency collar, is not
removed later in the collar.  Hence a coordinate of `V_p` fails to lie in
all `q+1` states ending at `p` exactly when it is one of
`beta_(p-q),...,beta_(p-1)`.  This proves (1.4).

Advance the endpoint once.  The oldest arrival `beta_(p-q)` is now present
throughout the new depth-`q` window, and this is the only new coordinate
that can enter the union of the two envelopes.  Iterating for
`v=0,...,ell-1` gives (1.5).  All displayed arrivals are distinct, giving
(1.6).  \(\square\)

The protection hypothesis is necessary.  The rank-two Johnson walk

\[
    12,\ 23,\ 12
\]

is adjacent at both steps, but it is not geodesic on the two-step collar;
its depth-two intersection is `{2}`, of rank one rather than `2-2=0`.
Thus neither adjacency nor a scalar phase label alone implies the theorem.

## 2. The flat-phase shift theorem

A generalized `G=0` schedule of deadline `d` comes with an **actual local
horizon** `rho(i)`.  Define its phase loss by

\[
    f(i)=d-\rho(i).                                   \tag{2.1}
\]

In the monotone generalized-flat schedules used by carrier 3, `f(i)` is the
number of preceding flat walls: across a strict edge `rho` is unchanged and
across a flat wall it falls by one.  In a more general deadline schedule a
raw repeated owner need not be a net phase wall, so all statements below use
the actual horizon `rho`, not a raw duplicate count.  A constant-phase piece
has one value `q` of `rho` throughout its protected interior.

Moving the same oriented inherited block past `t` further flats leaves its
internal event word unchanged but changes its local horizon from `q` to
`q-t`.  Here and below

\[
    0\le t\le q.                                      \tag{2.2}
\]

### Theorem 2.1 (exact flat-phase transport)

Let `U_q^V(p,ell)` be protected, and assume the same collar supports horizon
`q-t`.  Then

\[
\boxed{
 U_{q-t}^V(p,\ell)=U_q^V(p,\ell)\ \dot\cup\
 \{\beta_{p-q+\ell-1},\ldots,
   \beta_{p-q+t+\ell-2}\}.}                         \tag{2.3}
\]

The second set has exactly `t` coordinates.  Consequently

\[
    U_q^V(p,\ell)\subset U_{q-t}^V(p,\ell),
    \qquad
    |U_{q-t}^V(p,\ell)|=|U_q^V(p,\ell)|+t.            \tag{2.4}
\]

For proper-prefix compiler cells, the transported widths are

\[
    1\le\ell\le q-t.                                  \tag{2.5}
\]

The old widths `q-t+1,...,q` are explicit truncation casualties.  Any cell
whose dependency collar meets a physical cut is a seam casualty and is not
covered by this theorem.

#### Proof

Apply (1.5) with `q` and with `q-t`.  Since

\[
 E_{q-t}^V(p)=E_q^V(p)\dot\cup
 \{\beta_{p-q},\ldots,\beta_{p-q+t-1}\},
\]

the two consecutive-arrival ranges combine, and cancellation of the common
initial range gives exactly (2.3).  Equations (2.4) and (2.5) follow.
\(\square\)

Thus the rank spectrum of a protected phase-`q` row,

\[
    r-q,r-q+1,\ldots,r-1,
\]

becomes

\[
    r-q+t,r-q+t+1,\ldots,r-1.                         \tag{2.6}
\]

If `u` records provider rank and `v` records a fixed top tag, transport of
the surviving part multiplies its rank/tag polynomial by `u^t`, separately
in each `v`-sector.  This is an exact labelled statement, not merely a rank
count: (2.3) names the added arrival strip.

## 3. Pascal facets of arbitrary order

Let `Z_a` be a fixed `a`-set disjoint from `Omega`.  On a sufficiently
protected parent stream `V`, define the order-`a` Pascal facet

\[
    P^{(a)}_i(V)=Z_a\cup\bigcap_{v=0}^{a}V_{i+v}.
                                                        \tag{3.1}
\]

On a geodesic `a`-step parent window the intersection has rank `r-a`, so
`P^(a)` again has rank `r`.  Order zero is the no-top rail.  For `a=1` and
`Z_1={z}`, (3.1) is the usual top rail

\[
    \{z\}\cup(V_i\cap V_{i+1}).                       \tag{3.2}
\]

### Theorem 3.1 (Pascal envelope identity)

Whenever the displayed dependency collars are protected,

\[
\boxed{
 E_q^{P^{(a)}}(p)=Z_a\cup E_{q+a}^V(p+a),
 \qquad
 U_q^{P^{(a)}}(p,\ell)=Z_a\cup U_{q+a}^V(p+a,\ell).}
                                                        \tag{3.3}
\]

Hence every order-`a` provider has total rank

\[
    a+[r-(q+a)+\ell-1]=r-q+\ell-1,                    \tag{3.4}
\]

independent of `a`.  Moving this inherited piece past `t` flats shifts its
surviving providers upward by exactly `t` ranks, with the fixed tag `Z_a`
unchanged.

#### Proof

Intersect (3.1) for indices `p-q,...,p`.  The parent index intervals
`[p-q,p-q+a],...,[p,p+a]` have union `[p-q,p+a]`, so their intersection is
the parent depth-`q+a` envelope ending at `p+a`.  This proves the first
identity.  Taking `ell` consecutive unions proves the second.  Equation
(3.4) follows from Lemma 1.1, and Theorem 2.1 gives the flat shift.
\(\square\)

In the order-one odd-even lift, the no-top cell and its top mate are

\[
    U_q^V(p,\ell),
    \qquad
    \{z\}\cup U_{q+1}^V(p+1,\ell).                   \tag{3.5}
\]

They have the same total rank.  The old-coordinate core of the top cell has
rank one less.  If the no-top and top cells use aligned provider starts and
the top old cores are the same labelled families one rank lower, then the
total-rank Pascal layers have the form

\[
    \mathcal P_a=\mathcal A_a,
    \qquad
    \mathcal P_s=\mathcal A_s\sqcup
          (\{z\}+\mathcal A_{s-1})\quad(s>a).          \tag{3.6}
\]

Theorem 2.1 shifts both summands of every surviving layer together.

The preceding identities concern the chronology and its maximal envelopes.
They do not by themselves transport an arbitrary literal source assignment.

### Proposition 3.2 (facet transparency for a literal compiler)

Let `0<=a<=D`, and let nonempty parent source letters `A_j` realize
depth-`D` parent owners by

\[
    P_i=\bigcup_{j=i}^{i+D}A_j.                       \tag{3.7}
\]

The order-one facet core `P_i intersect P_(i+1)` is realized by the inherited
overlap letters `A_(i+1),...,A_(i+D)` if and only if

\[
\boxed{
 P_i\cap P_{i+1}=\bigcup_{j=i+1}^{i+D}A_j.}           \tag{3.8}
\]

For order `a`, the corresponding owner-core identity is

\[
\boxed{
 \bigcap_{u=0}^{a}P_{i+u}
    =\bigcup_{j=i+a}^{i+D}A_j.}                       \tag{3.9}
\]

If literal lower occurrences are to be inherited as well, (3.8) or (3.9)
must hold hereditarily on every selected provider interval after restriction
to its physical overlap.  In addition, every selected order-`a` interval
must actually hit every coordinate of the fixed tag `Z_a`; central owner
realization alone does not force a proper subinterval to contain the tag.
The conjunction of hereditary core equality and this tag-hit condition is
called **facet transparency**.

#### Proof

Every overlap letter on the right of (3.8) occurs in both owner windows, so
the right side is always contained in the left.  Equality is exactly the
assertion that the inherited overlap realizes the facet core.  The same
window-intersection argument proves (3.9).  Restricting it to each selected
provider, and requiring every fixed tag there, is plainly necessary and
sufficient for literal occurrence transport.  \(\square\)

Owner realization alone does not imply facet transparency.  At depth one,
take

\[
 A_0=\{x,a\},\qquad A_1=\{b\},\qquad A_2=\{x,c\}.
\]

Then `P_0={x,a,b}` and `P_1={x,b,c}`, so
`P_0 intersect P_1={x,b}` while the inherited overlap is only `{b}`.  For a
maximal erosion assignment the transparent identities can be checked
directly from the protected event formulas; they are not consequences of
owner equations alone.  Arbitrary lower-pin deletions may break them.

### Corollary 3.3 (the one-flat Pascal tower)

Let a protected full-phase no-top block of deadline `d` supply labelled
families

\[
   \mathcal A_s\quad(r-d\le s\le r-1)
\]

at its successive proper widths.  Suppose its order-one top copy is
facet-transparent (including the fixed-tag hit), is placed immediately after
one net phase wall, uses the same aligned provider starts, and loses no
displayed dependency collar at an endpoint or cut.  Then the protected
combined provider table is

\[
\boxed{
 \mathcal A_{r-d}\ \sqcup\!
 \bigsqcup_{s=r-d+1}^{r-1}
   \bigl(\mathcal A_s\sqcup
          (\{z\}+\mathcal A_{s-1})\bigr).}            \tag{3.10}
\]

Without hereditary core equality and fixed-tag hits, (3.10) remains a
correct maximal-envelope rank/tag ledger but need not be a set-labelled
literal provider table.

#### Proof

The no-top phase-`d` widths `1,...,d` have ranks `r-d,...,r-1` by
(1.6).  The top piece has local horizon `d-1`; by (3.3), its widths
`1,...,d-1` are `{z}` plus parent depth-`d` cells, so their old-coordinate
ranks are `r-d,...,r-2` and their total ranks are `r-d+1,...,r-1`.
Facet transparency identifies these cores with the displayed labelled
families.  \(\square\)

## 4. The sharp phase-credit criterion

Suppose every protected internal one-run of the parent has length at least
`D+1`; call this parent depth `D`.  A Boolean one-run of length `L` becomes
one of length `(L-a)^+` after the order-`a` intersection in (3.1).  Suppose
the parent atlas has already supplied its selected tight flags through every
depth at most `D`.  Suppose the child deadline is `d` and the piece has
actual phase loss `f`, where `0<=f<=d`.  Its local horizon is

\[
    q=d-f.                                             \tag{4.1}
\]

### Theorem 4.1 (phase credit)

A depth-`D` protected parent atlas automatically supplies the internal
residence and makes every **already selected parent flag** required by an
order-`a` piece at phase (4.1) available provided

\[
\boxed{f+(D-d)\ge a.}                                 \tag{4.2}
\]

As a universal depth-availability/residence implication, (4.2) is sharp.
It does not create a target label absent from the parent atlas.

#### Proof

For flags, (3.3) asks for parent depth at most

\[
    q+a=d-f+a,
\]

which is at most `D` exactly when (4.2) holds.  For residence, the shortest
allowed parent run has length `D+1`; after order-`a` intersection it has
length at least `D+1-a`, which is at least the required `q+1=d-f+1` under
the same inequality.

If (4.2) fails, a binary parent trace with one protected run of exact length
`D+1` produces a child run of length `D+1-a<d-f+1`.  Thus depth `D` alone
cannot imply the desired child residence.  Endpoint runs and cut-crossing
runs remain collar conditions in both directions.  \(\square\)

For the order-one facet used in an odd-even lift:

- on a depth drop `D=d+1`, (4.2) holds with `f=0`;
- on a plateau `D=d`, (4.2) requires `f>=1`, unless an independently
  depth-`d+1` facet package is supplied.

This is the exact residence benefit of putting a fragile intersection piece
after the first flat.

## 5. Shifted Pascal Hall towers

The next statement separates the unavoidable shifted-diagonal count from
physical compiler compatibility.

Let `A_s` be disjoint no-top label families, and define Pascal layers as in
(3.6):

\[
    \mathcal P_a=\mathcal A_a,
    \qquad
    \mathcal P_s=\mathcal A_s\sqcup
       (\{z\}+\mathcal A_{s-1})\quad(a<s\le b).         \tag{5.1}
\]

Fix `0<=t<=b-a+1`, and let `D_s subseteq P_s`.  Consider a bipartite
compiler subgraph with left
shore

\[
    X=\bigsqcup_{s=a}^{b}\mathcal P_s                 \tag{5.2}
\]

and right shore `Y`.  Assume there is exactly one right cell `c_T` for every

\[
    T\in\bigsqcup_{s=a+t}^{b}(\mathcal P_s\setminus D_s),
                                                        \tag{5.3}
\]

there are no other right cells in `Y`, and every `c_T` is adjacent to its
own label `T`.  Other cross-adjacencies are allowed.

### Theorem 5.1 (exact shifted-tower deficiency)

Under (5.1)--(5.3),

\[
\boxed{
 |X|-\nu(X,Y)=
 \sum_{s=a}^{a+t-1}|\mathcal P_s|+
 \sum_{s=a+t}^{b}|D_s|.}                              \tag{5.4}
\]

Here `nu(X,Y)` is the maximum matching size.  One new private cell for every
label counted on the right of (5.4) is sufficient to saturate `X`, and no
smaller cell augmentation can do so.

#### Proof

The own-label edges `T-c_T` form a matching saturating `Y`; hence
`nu(X,Y)=|Y|`.  Subtracting the cardinality in (5.3) from (5.2) gives
(5.4).  Adding the omitted private cells extends the own-label matching to
all of `X`.  Each new cell raises matching size by at most one, proving
minimality.  \(\square\)

The theorem is exact only under its displayed diagonal-cell hypothesis.  A
rank count without own-label adjacency is not enough.

## 6. Carrier 3 and the six-piece odd-even lift

For the authenticated carrier-3 Hall shore, put

\[
 |\mathcal A_5|=19,\qquad
 |\mathcal A_6|=94,\qquad
 |\mathcal A_7|=293.                                  \tag{6.1}
\]

Then

\[
\begin{aligned}
 X={}&\mathcal A_5\\
 &\sqcup(\mathcal A_6\sqcup(\{z\}+\mathcal A_5))\\
 &\sqcup(\mathcal A_7\sqcup(\{z\}+\mathcal A_6)),   \tag{6.2}
\end{aligned}
\]

whereas the exact-envelope right shore is

\[
\begin{aligned}
Y={}&(\mathcal A_6\setminus\{\mathtt{4c29}\})
       \sqcup(\{z\}+\mathcal A_5)\\
 &\sqcup(\mathcal A_7\setminus
       \{\mathtt{4879},\mathtt{4c39}\})
       \sqcup(\{z\}+\mathcal A_6).                  \tag{6.3}
\end{aligned}
\]

The own-label matching is independently authenticated.  Theorem 5.1 with
`a=5`, `b=7`, `t=1` gives

\[
    519-497=|\mathcal P_5|+1+2=19+1+2.                \tag{6.4}
\]

With `u` marking total rank and `v` the top tag, the stronger typed identity
is

\[
\begin{aligned}
L={}&19u^5+(94+19v)u^6+(293+94v)u^7,\\
R={}&(93+19v)u^6+(291+94v)u^7,\\
L-R={}&19u^5+u^6+2u^7.                                \tag{6.5}
\end{aligned}
\]

Both top diagonals survive.  The `1+2` losses are three no-top seam/private
motif exceptions; they are not an automatic cost of one flat.  The
carrier-3 audit identifies the nineteen rank-five cells with the moved
block's uncompensated bottom diagonal.  Thus carrier 3 is an exact
calibration of Theorems 2.1 and
5.1, not evidence that every flat schedule has the same three exceptions.

Now compare the six-piece odd-even lift.  Let `D` be the odd parent depth
and `d` the even child deadline.

- If `d=D-1`, as in the authenticated `11->12` and `13->14` lifts, the
  order-one intersection rail satisfies (4.2) before any flat.  There is no
  forced phase shift of its compiler tower.
- If `d=D`, as on the `15->16` plateau, the raw intersection rail loses one
  unit of residence.  Putting it after one flat makes its local horizon
  `d-1`, so (4.2) holds, but Theorem 2.1 shifts every surviving compiler
  diagonal of that moved piece upward by one rank and truncates its old
  bottom width.  This is not yet a global Hall loss: a full-phase no-top
  piece or an inverse-phase collar can supply the same target layer.

Therefore the local moved-block ledger is exact:

\[
 \boxed{\text{one recovered residence unit}
        \quad\longleftrightarrow\quad
        \text{one moved-block Pascal diagonal to compensate}.} \tag{6.6}
\]

Carrier 3's actual loss of all nineteen `A_5` labels is the independently
audited fact (6.2)--(6.5), not a universal consequence of (6.6).

The ordinary six-piece theorem is a uniform-depth theorem.  After mixed
phase placement, its length-`d+1` top ear, singleton slot, generalized
envelopes, and common compiler must all be replayed; none follows from
(6.6) alone.

## 7. The exact plateau-braid hypothesis

This section states the reusable missing assertion without hiding it behind
scalar capacity.

Fix a proposed generalized-flat child chronology `T`, its six-piece (or
multi-piece) decomposition, its phase map, and its protected interior
matching.  Let

- `C_prot` be the physical proper-prefix cells wholly inside protected
  dependency collars;
- `M_prot` be a fixed matching from the targets retained on those cells;
- `T_cas` be every remaining strict lower target, including targets whose
  designated providers belong to the bottom shifted diagonals, are
  truncated by flats, cross cuts, or are explicitly deleted seam/private
  labels;
- `C_free` be every physical proper-prefix cell not allocated by `M_prot`,
  including unallocated protected cells and all seam, ear, fan,
  inverse-phase, and collar cells.

Let `E_p` be the exact maximal source envelope at physical source position
`p`.  For a choice of nonempty source letters

\[
    \varnothing\ne Q_p\subseteq E_p,                  \tag{7.1}
\]

write

\[
    H_Q(T,C)=1
    \quad\Longleftrightarrow\quad
    \bigcup_{p\in C}Q_p=T.                            \tag{7.2}
\]

### Hypothesis `PBP(r,d)` (phase-balanced protected braid)

There is a generalized-flat braid satisfying all of the following.

1. **Phase credit and protected transport.**  Every order-`a_j` inherited
   piece with actual phase loss `f_j` satisfies
   
   \[
       f_j+(D_j-d)\ge a_j,
   \]
   and every cell used by `M_prot` has its full dependency collar.  Its
   exact-envelope labels are transported by (2.3) and (3.3), not merely by
   rank.  Every physically inherited literal facet provider also satisfies
   the full facet-transparency condition of Proposition 3.2, including its
   fixed-tag hit.
2. **One common source.**  A single family `Q=(Q_p)` satisfies (7.1) and the
   exact variable-horizon central reconstruction equations
   
   \[
       T_i=\bigcup_{p=i}^{i+\rho(i)}Q_p
   \]
   for every middle owner of `T`.
   Every edge of `M_prot` remains exact under this same `Q`.
3. **Full-signature casualty matching.**  The graph on
   `T_cas` and `C_free` with edges (7.2) has a matching saturating
   `T_cas`.  Equivalently, after `Q` is fixed, every casualty has a distinct
   literal physical interval with exactly its target union.  This includes
   mandatory-envelope and every-position hit constraints automatically.
4. **Physical seams.**  The braid has exact middle ownership, literal
   residence at the local phases, and complete arbitrary-width upper target
   coverage: every internal inherited upper witness is retained or replayed,
   and every old/new seam-crossing window is included in the literal
   six-piece `I_q union N_q` audit.  It also has legal endpoints/terminal
   suffix and a literal top-singleton source when the even lift requires
   one.

`PBP(r,d)` is the precise braid hypothesis left unproved in this note.

### Theorem 7.1 (plateau closure under `PBP`)

If the odd-even generalized six-piece construction satisfies
`PBP(r,d)`, then its literal source word is universal.  If its middle rows
are exactly the `W=binom(2r,r)` distinct owners and its source has the
deadline-tight `W+d` positions, its length is `B(2r)=W+d`.

#### Proof

The protected matching and the casualty matching together cover every
strict lower target using one common literal source `Q`.  The central
reconstruction equations cover every middle owner.  Physical-seam clause 4
covers every upper target by a literal interval and supplies all endpoint
and top-singleton obligations.  Hence the source word covers every nonempty
mask.  The deadline ledger gives its stated length.  \(\square\)

### Proposition 7.2 (minimality relative to frozen interiors)

Fix `T`, the protected pieces, `M_prot`, and let `C_free` contain every
physical proper-prefix cell not allocated by `M_prot`.  Among source words
that reconstruct this fixed `T` and leave `M_prot` intact, clauses 2 and 3
of `PBP` are necessary and sufficient for completing the strict lower
compiler.

#### Proof

Necessity follows by taking the actual nonempty letters of any completing
word and one actual witnessing interval for every target not covered by
`M_prot`.  One interval has one union, so witnesses for distinct target
labels are distinct.  Sufficiency is exactly the union of the two
matchings.  \(\square\)

This relative statement does not say every global completion must preserve
the chosen interiors or Hall shore.  A different chronology may destroy and
rebuild them.

The typed phase-balance identity

\[
    \sum_j u^{t_j}F_j^{\rm surviving}+F_{\rm seam}
       =F_{\rm required}                              \tag{7.3}
\]

is necessary for a diagonal-preserving realization, but not sufficient for
`PBP`: labels and one common `Q` still matter.  For example, a cell whose
allowed mask is `{1,2}` but whose mandatory mask is `{2}` cannot serve the
target `{1}`, regardless of rank balance.

## 8. Exact all-`k` implication and current obstruction

The proved reusable implication is conditional but sharp:

### Corollary 8.1

Suppose every odd-even deadline step admits a phase-balanced protected braid
whose parent pieces come from exact odd carriers, suppose the odd recursion
supplies the corresponding protected atlases, and suppose each resulting
child has exactly `W` middle owners and `W+d` source positions.  Then each
even step attains its deadline bound.  At a depth drop, order-one pieces may be
placed in phase zero.  At a plateau, every fragile order-one piece must
either receive one flat of phase credit or use a depth-`d+1` parent package,
and every flat-shifted bottom diagonal must be supplied by the casualty bank
of `PBP`.

No known theorem proves this existence assertion.  In particular:

- complete owner and all-depth shadow decks do not imply protected
  geodesic collars;
- the rank/tag identity (7.3) does not imply full-signature Hall;
- separate sector compilers do not imply one common `Q`;
- the top ear does not by itself replace a shifted bottom diagonal;
- rotations and orientations do not force the required seam labels.

Carrier 3 proves that the missing bank can be macroscopic even when its
shape is perfectly Pascal: the exact exposed tower is `19+1+2`.  The later
cross-reflection halo reduces its concrete Hall deficit to three, showing
that nonlocal braiding can transport most of the tower, but its remaining
lower units and upper seam chains are still coupled.  This is consistent
with `PBP` and does not prove it.

The smallest exact positive all-`k` lemma now sought is therefore:

> **Plateau braid existence lemma (UNPROVED).**  For every plateau parent
> in a specified PBBS/Pascal family, one can choose the six-piece cuts,
> phases, orientations, and a protected seam/inverse-phase bank so that
> clauses 1--4 of `PBP(r,d)` hold.

It is enough to prove this for one explicit recursive carrier family.  A
counterexample must fail one named clause: phase credit, labelled protected
transport, common-`Q` casualty Hall, or physical upper/seam replay.  Scalar
capacity failure or success alone is not decisive.

## 9. Independent audit

The decisive identities were derived in two independent ways.

1. The event-stream audit expanded (1.4)--(2.3) coordinate by coordinate and
   checked every off-by-one range.  It independently recovered the typed
   carrier-3 polynomial (6.5) and the exact `19+1+2` deficiency.
2. The Pascal audit derived (3.3) directly from nested intersections and
   independently obtained the phase-credit inequality (4.2).  It also
   checked the depth-drop/plateau distinction against the authenticated
   `11->12`, `13->14`, and carrier-3 `15->16` data.

The audit rejected three stronger interpretations:

- unprotected Johnson adjacency is insufficient (`12,23,12`);
- shifting ranks does not transport mandatory masks or common-`Q` choices;
- the mixed-phase theorem does not inherit the uniform-depth six-piece ear
  and seam conclusions without literal replay.

No computation or finite search was used in proving the general theorems.
