# PBBS-to-product-SCD annuli: exact baseline overlay and the local second-baseline obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

The exterior estimate used below is the exact product-SCD quantifier in
`MATH_AUDIT_PRODUCT_SCD_TAIL_EXACT_GAUSSIAN_QUANTIFIER_20260726.md`.
The delayed-atom specialization in Section 6 uses
`MATH_THEOREM_O_ABSTRACT_OWNER_CYCLE_LITERAL_COMPILER_INTERFACE_20260726.md`,
and the physical local rotor splice is the absorber in
`MATH_THEOREM_N_TWO_COLOR_PRODUCT_SCD_PHYSICAL_ENDPOINT_FUSION_20260726.md`.

## 0. Outcome

Let

\[
 W=\binom{2m}{m}.
\]

Suppose a PBBS-derived word of length \(W+o(W)\) already covers a
sub-Gaussian central band through depth

\[
 h=o(\sqrt m).
\]

Choose an exterior cutoff \(d\) with

\[
 \sqrt m\ll d=o(m).
\]

The established product-SCD word covers every depth larger than \(d\) in
\(o(W)\) further letters.  The open problem is the annulus

\[
 h<q\le d.
\]

This note proves three exact statements about a direct compiler for that
annulus.

1. **There is an explicit local product-diagonal OR chart.**  For every
   pair of symmetric chains, its middle diagonal has \(\ell\) owners and
   its complete sub-root rectangle has a nonzero literal word of length
   \(2\ell-1\), or \(2\ell-2\) in the unique empty-core cell.  Every
   lower and upper sub-root flag is a contiguous interval in this word.

2. **Independent local replacement is coefficient-scale fatal.**  If
   every chain-pair cell is compiled in its own word block while retaining
   its middle owners and the lower annulus beyond depth \(h\), then

   \[
    \boxed{
    L_{\rm sep}\ge
    2W-(m+1)-(2h+3)(p_0-1),}
   \]

   where

   \[
    p_0=\binom m{\lfloor m/2\rfloor}^{\!2}
       =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.
   \]

   Hence \(h=o(\sqrt m)\) forces

   \[
    \boxed{L_{\rm sep}\ge(2-o(1))W.}
   \]

   The explicit local charts have total length

   \[
    2W-p_0-1=(2-o(1))W,
   \]

   so the obstruction is asymptotically sharp.  Calling the middle
   diagonals a baseline credit does not save the construction: a second
   baseline is still spent.

3. **A genuine in-place annulus has an exact overlay formulation.**  A
   family of PBBS and product-SCD atom templates may be placed in one
   master order.  At each master position take the union of all atoms
   placed there.  If every template order is preserved and every foreign
   atom lying between the endpoints of a selected witness is contained in
   its target, then all selected PBBS and annulus targets remain literal
   contiguous ORs.  Thus a master overlay of length \(W+o(W)\), followed
   by the \(o(W)\) exterior tail, is a coefficient-one compiler.  Its
   length is the master length plus the tail; the old \(W\) is not added
   again.

The overlay condition is constructive and exact, but its global
existence is not proved.  The local lower bound shows what it must do:
merge a positive density of atom positions belonging to different
chain-pair cells, and in the PBBS hybrid merge those atoms into positions
of the already-paid PBBS word.  The existing safe product-path absorbers
solve individual physical seams; they do not prove the required global
order-and-cap overlay or its all-depth target-column Hall condition.

The product-SCD charts and tail transfer to odd dimension by the standard
trimmed one-coordinate lift.  The overlay theorem itself is
dimension-independent, so the odd lifted templates may be overlaid
directly with the actual odd PBBS word; that PBBS word need not be an even
lift.  The product baseline and every displayed product error double,
while

\[
 \binom{2m+1}{m}\sim2\binom{2m}{m},
\]

so all normalized conclusions are unchanged.

## 1. Product-SCD rectangles and their middle diagonals

Split the ground set as

\[
 V=A\mathbin{\dot\cup}B,
 \qquad |A|=|B|=m,
\]

and fix symmetric-chain decompositions of \(2^A\) and \(2^B\).  Let

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a},
 \qquad
 D_b\subset D_{b+1}\subset\cdots\subset D_{m-b}
\]

be two chains, indexed by rank.  Put

\[
 c=\max(a,b),
 \qquad
 \ell=m-2c+1.
 \tag{1.1}
\]

The rank-\(m\) diagonal of their product rectangle is

\[
 X_i=C_i\cup D_{m-i},
 \qquad c\le i\le m-c.
 \tag{1.2}
\]

It has exactly \(\ell\) owners.  Every middle set belongs to a unique
pair of SCD chains and to exactly one diagonal (1.2).  Consequently all
nonempty diagonals partition the middle layer and

\[
 \boxed{\sum_{C,D}\ell(C,D)=W.}
 \tag{1.3}
\]

The number of diagonals is

\[
 \boxed{
 p_0=\binom m{\lfloor m/2\rfloor}^{\!2}.}
 \tag{1.4}
\]

Indeed an SCD contains one member of each chain in the middle rank, so
the number of chains is the central binomial coefficient.  Stirling's
formula gives the asymptotic in Section 0.

### Lemma 1.1 (exact diagonal trace identities)

Suppose \(u,v\in[c,m-c]\).

* If \(u+v=m-q\), then

  \[
   \boxed{
   C_u\cup D_v
    =\bigcap_{i=u}^{m-v}X_i.}
   \tag{1.5}
  \]

* If \(u+v=m+q\), then

  \[
   \boxed{
   C_u\cup D_v
    =\bigcup_{i=m-v}^{u}X_i.}
   \tag{1.6}
  \]

In both cases the owner interval has \(q+1\) states.

#### Proof

Along (1.2), the \(A\)-component increases and the \(B\)-component
decreases.  In (1.5), the smallest \(A\)-rank is \(u\), while the
smallest \(B\)-rank is

\[
 m-(m-v)=v.
\]

Intersections of nested chain members therefore give \(C_u\cup D_v\).
The number of transitions is \(m-v-u=q\).  For (1.6), the largest
\(A\)-rank is \(u\), and the largest \(B\)-rank occurs at \(i=m-v\)
and equals \(v\).  Unions give the stated target, again across \(q\)
transitions. \(\square\)

Thus the diagonal path is a literal two-signed flag atlas for the
sub-root square \([c,m-c]^2\).  Targets outside this square are the corner
part of the product rectangle; the full product-chain word used below
also represents them.

## 2. The exact local OR chart

For \(c\ge1\), write the saturated-chain increments as

\[
 C_j=C_c\cup\{x_{c+1},\ldots,x_j\},
 \qquad
 D_j=D_c\cup\{y_{c+1},\ldots,y_j\},
 \tag{2.1}
\]

and put

\[
 G=C_c\cup D_c.
\]

Define

\[
 \boxed{
 Q_{C,D}=
 \{x_{m-c}\},\ldots,\{x_{c+1}\},
 G,
 \{y_{c+1}\},\ldots,\{y_{m-c}\}.}
 \tag{2.2}
\]

Every letter is nonempty, and

\[
 |Q_{C,D}|=2\ell-1.
 \tag{2.3}
\]

### Theorem 2.1 (sub-root rectangle compiler)

The word (2.2) represents every set

\[
 C_u\cup D_v,
 \qquad c\le u,v\le m-c.
 \tag{2.4}
\]

In particular it represents every middle owner (1.2) and every lower and
upper target in Lemma 1.1.

#### Proof

If \(u>c\), begin at the letter \(\{x_u\}\); if \(u=c\), begin at
\(G\).  Read through \(G\), and, if \(v>c\), continue through
\(\{y_v\}\).  The union is

\[
 C_c\cup D_c
 \cup\{x_{c+1},\ldots,x_u\}
 \cup\{y_{c+1},\ldots,y_v\}
 =C_u\cup D_v.
\]

The displayed letters are consecutive in (2.2). \(\square\)

There is one exceptional chain pair with \(a=b=c=0\).  Its core \(G\)
is empty and cannot be emitted.  Delete that one letter from (2.2).  The
resulting \(2m=2\ell-2\) nonempty letters still represent every nonempty
set in the rectangle: a target on one axis is a suffix of the left arm or
a prefix of the right arm, and a target using both shores crosses their
common seam.  The omitted target is only the empty set.

Summing these charts over all chain pairs gives the exact length

\[
 \boxed{
 \sum_{C,D}|Q_{C,D}|=2W-p_0-1.}
 \tag{2.5}
\]

This is a direct, integral OR compiler, but it is not coefficient one.

For reference, the complete product-rectangle template is

\[
 \operatorname {rev}R(C),R(D),
 \tag{2.6}
\]

where \(R(C)\) and \(R(D)\) are the usual nonempty forward increment
words of the two SCD chains.  It represents every nonempty
\(C_u\cup D_v\), including the corner part excluded from (2.4).  Thus
the collection of templates (2.6), restricted to selected witness
intervals, supplies a literal template for every target in the annulus.

## 3. A sharp local second-baseline lower bound

Fix \(h\ge0\).  Call a compiler *cell-separated* if its word is a
concatenation of disjoint chain-pair blocks and every selected witness for
a target assigned to \((C,D)\) is wholly inside that pair's block.  The
block may use arbitrary nonempty set letters; it need not use (2.2).

For a cell with \(c\ge1\), put

\[
 r=\ell-1=m-2c,
 \qquad
 R=(r-h-1)_+= (\ell-h-2)_+.
 \tag{3.1}
\]

When \(R>0\), consider the two lower-annulus axes

\[
 A_j=C_{c+j}\cup D_c,
 \qquad
 B_j=C_c\cup D_{c+j},
 \qquad 0\le j\le R.
 \tag{3.2}
\]

They have lower depths

\[
 q_j=r-j\ge h+1.
 \tag{3.3}
\]

### Lemma 3.1 (two-axis pin bound)

Any nonzero word representing all sets in (3.2) has at least

\[
 \boxed{2R+1}
 \tag{3.4}
\]

positions.

#### Proof

Choose one witness for \(A_j\).  For every \(1\le j\le R\), that
witness contains a position whose letter contains the new pin \(x_{c+j}\).
Every letter in this witness is a subset of \(A_j\).  Hence the chosen
position for pin \(x_{c+j}\) cannot equal a position chosen at an earlier
level \(i<j\), because the latter is contained in \(A_i\) and excludes
\(x_{c+j}\).  This gives \(R\) distinct left-pin positions.

The same argument gives \(R\) distinct right-pin positions containing
the \(y_{c+j}\)'s.  A left-pin position cannot be a right-pin position:
the former is contained in some \(A_i\), which contains no right pin,
whereas the latter contains one.  Finally a witness for

\[
 A_0=B_0=G
\]

contains a position whose letter is a nonempty subset of \(G\).  That
position contains no left or right pin and is new.  The total is
\(2R+1\). \(\square\)

The \(\ell\) middle owners in (1.2) also force at least \(\ell\)
positions.  Indeed distinct equal-rank sets cannot be witnessed by
intervals with one common left endpoint: such intervals have nested
unions, and equal-cardinality comparable sets are equal.  Thus their
witnesses have distinct left endpoints.

### Theorem 3.2 (cell-separated annulus obstruction)

If a cell-separated compiler represents every middle owner and all lower
targets of depths \(h+1,\ldots,r\) on every sub-root cell, then

\[
 \boxed{
 L_{\rm sep}
 \ge W+
   \sum_{(C,D):\,c\ge1}(\ell(C,D)-2h-3)_+.}
 \tag{3.5}
\]

Consequently

\[
 \boxed{
 L_{\rm sep}
 \ge2W-(m+1)-(2h+3)(p_0-1).}
 \tag{3.6}
\]

#### Proof

For one nonexceptional cell, Lemma 3.1 and the middle-antichain bound give

\[
 L_{C,D}\ge
 \max\{\ell,2\ell-2h-3\}
 =\ell+(\ell-2h-3)_+.
 \tag{3.7}
\]

The exceptional \(c=0\) cell still costs at least its \(m+1\) middle
owners.  Summing (3.7) and using (1.3) proves (3.5).

For every real \(x\), \((x-a)_+\ge x-a\).  The nonexceptional diagonal
lengths sum to \(W-(m+1)\), and there are \(p_0-1\) such cells.  Hence

\[
 \sum_{c\ge1}(\ell-2h-3)_+
 \ge W-(m+1)-(2h+3)(p_0-1),
\]

which gives (3.6). \(\square\)

If \(h=o(\sqrt m)\), equations (1.4) and (3.6) give

\[
 L_{\rm sep}\ge(2-o(1))W.
 \tag{3.8}
\]

Equation (2.5) supplies the matching upper coefficient.  The conclusion
already follows from one sign and only the two annulus axes.  Adding upper
targets, corner targets, or PBBS interface conditions cannot weaken it.

## 4. Exact master-overlay compiler

The obstruction in Section 3 is caused by keeping chain-pair blocks
separate.  We now state exactly what a successful nonlocal replacement
must provide.

An *atom template* is a finite sequence

\[
 \mathcal Q^\alpha=(Q_1^\alpha,\ldots,Q_{s_\alpha}^\alpha)
 \tag{4.1}
\]

of nonempty set letters, together with selected intervals
\([a,b]\subseteq[s_\alpha]\).  The target assigned to that interval is

\[
 T_{\alpha,a,b}=\bigcup_{j=a}^{b}Q_j^\alpha.
 \tag{4.2}
\]

Use one template for the already-paid PBBS word and the product templates
(2.6), retaining from the latter only the intervals whose targets lie in
the annulus.

### Definition 4.1 (legal order-and-cap overlay)

A legal overlay of the templates into \([L]\) consists of strictly
increasing maps

\[
 \iota_\alpha:[s_\alpha]\longrightarrow[L].
 \tag{4.3}
\]

At a master position \(z\), put

\[
 Z_z=\bigcup_{\alpha,j:\,\iota_\alpha(j)=z}Q_j^\alpha,
 \tag{4.4}
\]

and delete positions for which this union is empty.  The cap condition is
that, for every selected interval \([a,b]\) of every template,

\[
 \boxed{
 \iota_\alpha(a)\le z\le\iota_\alpha(b)
 \quad\Longrightarrow\quad
 Z_z\subseteq T_{\alpha,a,b}.}
 \tag{4.5}
\]

Condition (4.5) applies also to master positions occupied only by foreign
templates.  It is therefore stronger than pairwise equality of ports.

### Theorem 4.2 (exact annulus overlay compiler)

For every legal overlay, the master word

\[
 Z_1,Z_2,\ldots,Z_L
 \tag{4.6}
\]

represents every selected target of every template.

#### Proof

Fix \((\alpha,[a,b])\).  The atoms

\[
 Q_a^\alpha,\ldots,Q_b^\alpha
\]

occur in their original order between master positions
\(\iota_\alpha(a)\) and \(\iota_\alpha(b)\).  Their union is the target
by (4.2), so the union of the whole master interval contains the target.
Conversely (4.5) says that every master letter in the interval is a
subset of the target.  The union is therefore exactly the target.
\(\square\)

This theorem is the literal OR analogue of a rotor braid.  The maps
\(\iota_\alpha\) carry chronological order; the caps (4.5) certify that
all interleaved foreign atoms are harmless.  No averaging or cancellation
is present.

### Corollary 4.3 (in-place PBBS annulus ledger)

Assume the following data.

1. A PBBS template covers all signed depths \(q\le h\).
2. Product-SCD templates cover every target with \(h<q\le d\).
3. These templates have a legal overlay of length
   \(L=W+o(W)\).
4. The established product-SCD exterior word begins at depth \(d+1\).

Then one literal word covers all nonempty subsets and has length

\[
 \boxed{
 L+L_m(m-d-1)=W+o(W).}
 \tag{4.7}
\]

For odd dimension use the trimmed lift and replace the last tail term by
its exact odd double.

#### Proof

Theorem 4.2 covers the central PBBS band and the entire annulus in the
single master block.  The exterior product-SCD word covers the remaining
ranks.  Concatenation preserves every witness internal to either block.
Since \(d/\sqrt m\to\infty\), the uniform tail theorem gives
\(L_m(m-d-1)=o(W)\).  Crucially, the length is (4.7), not
\(W+L+L_m\): the PBBS baseline is one of the overlaid templates and has
already been counted in \(L\). \(\square\)

## 5. Baseline endpoint reuse is compulsory

The overlay theorem is a sufficient construction, but positive-density
baseline reuse is also necessary at the Gaussian inner edge.

### Theorem 5.1 (annular endpoint reuse)

Let a word of length \(W+e\) represent all \(W\) middle sets and all
\(N_q=\binom{2m}{m-q}\) sets at one lower depth \(q\).  After selecting
one witness for each target, at least

\[
 \boxed{N_q-e}
 \tag{5.1}
\]

lower targets share their left endpoint with a distinct middle-target
witness.  At a shared endpoint the lower target is contained in the
middle target.  The upper/right-endpoint analogue is identical.

#### Proof

Distinct equal-rank targets need distinct witness left endpoints, by the
nested-interval argument used in Section 3.  The middle starts form a
\(W\)-subset of the \(W+e\) word positions, and the lower starts form an
\(N_q\)-subset.  Their intersection has size at least

\[
 W+N_q-(W+e)=N_q-e.
\]

At a common left endpoint the two witness intervals are nested, so the
shorter union is contained in the longer one.  Their ranks determine that
the lower target is the contained set. \(\square\)

For \(q=\Theta(\sqrt m)\), one has \(N_q=\Theta(W)\).  Thus any
\(W+o(W)\) annulus compiler must reuse baseline endpoints for
\(\Theta(W)\) annulus targets.  Appending a separate product chart, even
one whose standalone coefficient is small for a large fixed Gaussian
cutoff, cannot meet this requirement.

## 6. Rotor specialization and the exact remaining gate

There is a structured way to seek an overlay.  Fuse the product-SCD
middle paths into long physical Johnson rows, then apply the delayed-atom
OR compiler to those rows.  If the fused atlas has \(K\) components, is
two-sided safe through depth \(d\), and has aggregate actual signed holes
\(\Delta_d\), its exact word length is

\[
 \boxed{
 W+2dK+\Delta_d.}
 \tag{6.1}
\]

Thus

\[
 K=o(W/d),
 \qquad
 \Delta_d=o(W)
 \tag{6.2}
\]

produce an in-place annulus replacement, after which the exterior tail is
\(o(W)\).  Formula (6.1) is another realization of Theorem 4.2: one base
atom is charged per middle owner, and only the outer cyclic collars and
actual target holes are additional.

The unfused product-SCD atlas has

\[
 K=p_0=\Theta(W/\sqrt m).
\]

When \(d/\sqrt m\to\infty\), its collar alone is \(\omega(W)\).  Hence
almost all diagonal paths must be fused.  The proved physical
\(Q_{R+1}\) two-cut absorber supplies a literal two-sided-safe fusion
when its four \((d-1)\)-fringes are disjoint.  It changes exactly \(2q\)
old columns into \(2q\) new columns at each sign and depth \(q\), but it
does not choose those columns globally.

The remaining theorem is therefore the following.

> **PBBS/product annulus overlay gate.**  Choose physical product-path
> orientations and safe rotor absorbers, or directly choose the maps
> \(\iota_\alpha\), so that:
>
> 1. the PBBS shallow templates and every product-SCD annulus template
>    obey one common master order;
> 2. the cap condition (4.5) holds for all selected lower and upper
>    witnesses;
> 3. the final number of owner components is \(o(W/d)\);
> 4. the aggregate all-depth signed target holes are \(o(W)\); and
> 5. the master word has \(W+o(W)\) positions.

The local second-baseline theorem proves that item 5 cannot be obtained by
concatenating or independently replacing chain-pair cells.  The physical
absorber proves that safe seams exist locally, but point-margin balance is
only a projection of items 2 and 4.  What is still missing is a
simultaneous target-column Hall/ordered-overlay theorem, or a sharp cut
showing that such an overlay is impossible.

## 7. Audited boundary

Proved here:

1. the exact product-diagonal lower and upper trace identities;
2. a nonzero \(2\ell-1\)-letter OR chart for every nonempty sub-root
   rectangle;
3. the exact global chart length \(2W-p_0-1\);
4. the asymptotically matching \((2-o(1))W\) lower bound for every
   cell-separated annulus compiler at \(h=o(\sqrt m)\);
5. the exact master-overlay sufficiency theorem;
6. the no-double-count in-place ledger (4.7); and
7. the positive-density endpoint-reuse necessity theorem.

Not proved:

1. a \(W+o(W)\) PBBS/product master overlay;
2. the all-depth two-sign column Hall theorem for the safe rotor
   absorbers; or
3. coefficient one.

The mathematical conclusion is sharp: the direct local annulus compiler
exists, but it costs a second baseline and is asymptotically optimal in
that class.  A coefficient-one compiler must be a genuinely nonlocal
cross-cell rotor/OR overlay which consumes the already-paid PBBS baseline
positions rather than sitting beside them.
