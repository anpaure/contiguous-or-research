# Split-letter finishing of a protected Catalan connector: exact positive face and component-type gate

Date: 2026-08-01  
Lane: H1 / protected Catalan connector / additive terminal compiler  
Status: exact conditional theorem and sharp scope obstruction.  The result
does not construct the Catalan connector.

## 0. Outcome

The split-letter theorem has a clean role after the protected Catalan
connector has been selected.

* A bounded family of ordinary lower, upper, or deeper **OR-mask debts** can
  be paid by the same bounded number of new source letters whenever every
  debt mask is contained in one actual old source letter, or more generally
  in the union of the two letters at a chosen cut.  Every old interval OR,
  every named protected witness, and an already selected residual closure are
  transported literally.
* A nested one-sided damage ray can be cheaper: one new letter pays the whole
  ray precisely under the frozen one-column criterion.
* The same operation does **not** merge components, create a missing rooted
  incidence edge, or restore a missing paired-upper occurrence in the
  Catalan forest.  Those are owner-layer resources rather than OR-mask
  values.

Consequently the split-letter pivot is a genuine bounded terminal finish for
the protected connector theorem, but not an absorber for its
`Cat_m-O(1)` connector edges.  The exact order is

\[
 \boxed{
 \text{rooted Catalan forest}
 \;\longrightarrow\;
 \text{connector forest and residual closure}
 \;\longrightarrow\;
 \text{bounded split-letter mask finish}. }
 \tag{0.1}
\]

The pentagonal rotation bank is compatible with this order: it preserves the
two immediate palettes exactly and can remove physical cycles in prepared
supports, but it does not by itself select the Catalan-scale connector.

## 1. Simultaneous block-contraction theorem

Let

\[
                         A=(A_0,\ldots,A_{N-1})            \tag{1.1}
\]

be a nonzero set word.  Let `D={T_1,...,T_H}` be a set of nonempty target
masks.  Partition `D` into (possibly empty) banks `D_r`, indexed by selected
source positions, and suppose

\[
                         T\subseteq A_r
             \qquad(T\in D_r).                            \tag{1.2}
\]

At each selected position replace `A_r` by the consecutive block

\[
                         A_r,(T:T\in D_r),                 \tag{1.3}
\]

in any fixed order.  Call the resulting length-`N+H` word `A^D`.

### Theorem 1.1 (bounded dominated-mask reset)

There is an injective order-preserving transport `Phi` from the interval
cells of `A` to those of `A^D` such that

\[
                 \operatorname{OR}_{A^D}(\Phi(I))
                    =\operatorname{OR}_{A}(I)             \tag{1.4}
\]

for every old interval `I`.  Every `T_i` is also realized by its new
singleton cell.  Hence `A^D` realizes the entire old OR deck together with
all of `D`.

Moreover, any finite certificate represented by named old interval cells is
transported literally: its mask values and their linear order are unchanged.
In particular an already selected protected residual closure and all its
named upper witnesses survive.

#### Proof

Map an old interval to the interval obtained by replacing every selected old
position which it contains by its whole block (1.3), and merely shift the
indices elsewhere.  This map is injective and preserves endpoint order.  The
union of a replacement block is `A_r` by (1.2), so replacing one or several
positions does not change the old interval union.  This proves (1.4).
Each `T_i` is a nonempty source letter and therefore occurs as a singleton.
Applying the same transport to every named cell proves the certificate
statement.  \(\square\)

No separation between the selected positions is required.  An old interval
may cross every replaced block: each block is individually OR-redundant.
The price is exactly one position per listed singleton task, not one position
per old witness which the task might otherwise damage.

### Corollary 1.2 (adjacent-union pivot reset)

Select any old cuts `c|c+1`.  At cut `c` insert a block of nonempty task
letters `D_c`, subject only to

\[
                     T\subseteq A_c\cup A_{c+1}
                         \qquad(T\in D_c).                \tag{1.5}
\]

Then every old interval OR and every named old certificate row transports
literally, while each inserted task occurs as a singleton.  Several cuts,
including adjacent cuts, may be used simultaneously.  For a fixed cut and
the natural endpoint transport, (1.5) is also necessary.

#### Proof

An old interval whose endpoints lie on one side of a cut gains none of its
inserted letters.  An old interval crossing that cut contains both adjacent
old letters, so every inserted task at that cut is OR-redundant by (1.5).
Apply this independently at every crossed cut.  Conversely, transport the
minimal old crossing interval `[c,c+1]`.  Its OR may not grow, so the union
of the inserted block, and hence each of its task letters, must be contained
in `A_c union A_(c+1)`.  \(\square\)

Thus the exact bounded finish needs only an **adjacent-union cover** of the
debt bank.  Domination by one actual source letter, as in (1.2), is the
stronger block-split face which is automatically compatible with replacing
that letter by a longer block.

### Corollary 1.3 (one-column compression)

Suppose instead that a bank `R_0,...,R_s` is to be realized by intervals
beginning at one new letter `Z` and ending along one old prefix chain.  One
new position suffices if and only if there are a task letter `T`, an actual
old letter `X=Z\cup T`, and old prefix unions `P_j` with

\[
                            R_j=Z\cup P_j.                 \tag{1.6}
\]

The reverse suffix version is identical.  Thus one split letter can absorb
an arbitrarily long nested ray, but not an arbitrary family of masks of the
same cardinality.  This is exactly the direct one-column criterion in
`MATH_THEOREM_H1_SPLIT_LETTER_RAY_ABSORPTION_AND_ONE_COLUMN_CRITERION_20260801.md`.

## 2. Exact protected-Catalan finish

Use the notation of the rooted connector decomposition.  Thus `M_0` is a
perfect incidence matching, `Q_0` is an upper-exact rooted Catalan forest,
and `Q_1` is a matching of `Cat_m-1` links which is a tree after contracting
the components of `Q_0`.  Assume their union is a spanning directed path,
and let `e_*` be the one residual incidence edge which closes that path.

Call this certificate **compiled and contraction-stable** in `A` when its
ordered owner occurrences, its lower-q1 rows, its chosen immediate-upper
occurrences, `e_*`, and every named protected upper witness are represented
by named interval cells whose allowed deadlines tolerate the block
transport of Theorem 1.1.  If a capped common-`Q` compiler conclusion is
desired, this phrase additionally requires the displayed expanded letters
to lie in their final caps and the transported rows together with the task
rows to pass the exact maximal common-`Q` criterion.  Without that extra
clause the theorem below is only an unrestricted interval-word statement.

### Theorem 2.1 (bounded terminal finish after the connector)

Assume:

1. `(M_0,Q_0,Q_1,e_*)` is a compiled, contraction-stable protected
   Catalan-connector certificate in `A`;
2. all remaining terminal defects are a set `D` of at most `H` ordinary
   OR-mask targets; and
3. `D` admits the domination assignment (1.2), the adjacent-union assignment
   (1.5), or is partitioned into one-column ray banks satisfying (1.6).

Then at additive cost at most `H` (and one per ray bank where (1.5) is used)
there is a nonzero word which retains:

* the full old interval deck;
* the protected owner chronology and lower-q1 rows;
* the paired immediate-upper occurrences selected by `Q_0`;
* the spanning-path topology and the protected residual closure `e_*`; and
* every target in `D`.

In particular the split operation creates no new upper, topology, or
common-cap casualty among the named old rows.

#### Proof

Apply Theorem 1.1 or Corollary 1.2 to singleton debts and Corollary 1.3 to
every chosen ray bank.  The first two transport every named certificate row
literally.  The latter is the same block-contraction argument with the
additional ray intervals displayed in (1.6).  By contraction stability, the transported
owner and incidence rows retain the same labels, order, and selected graph
edges.  Hence `Q_0`, `Q_1`, and `e_*` remain the same protected connector
certificate.  The newly created singleton or ray cells realize all of `D`.
No old OR row is deleted.  \(\square\)

The theorem is deliberately downstream of the connector construction.  A
missing ordinary mask and a missing paired occurrence of that mask are not
the same defect.

## 3. Component and paired-palette type obstruction

### Proposition 3.1 (component neutrality of block contraction)

Let `G` be any graph certificate on named old owner occurrences, with its
edge set also named before a block split.  If the final certificate uses only
the transported owner occurrences and transported edges, then it is
canonically isomorphic to `G`.  In particular

\[
                         c(G^D)=c(G).                      \tag{3.1}
\]

If `G` already uses every rank-`m` owner value once, every genuinely new
rank-`m` interval in the split word duplicates an existing owner label.
Using it in a simple spanning factor therefore requires deleting or
reassigning an old occurrence.  That is an owner-layer rethread, not a
consequence of block contraction.

#### Proof

The transport is a bijection from the named old owner occurrences and named
old edges to their images, preserving all labels and incidences.  It is
therefore a graph isomorphism.  Completeness of the old owner set proves the
duplicate-label statement.  \(\square\)

### Proposition 3.2 (paired-upper type mismatch)

Let `R` be a missing immediate-upper colour in a proposed rooted Catalan
forest.  Inserting `R` as a singleton source letter proves only that `R`
occurs in the interval-OR deck.  It does not choose an unused incidence edge
`e`, does not establish

\[
                         \operatorname{up}(e)=R,           \tag{3.2}
\]

does not free the tail and head of `e`, and does not preserve graphic
independence after adding `e`.  Hence split-letter coverage cannot repair a
deficiency of the matching/graphic rows defining `Q_0` or `Q_1`.

The same distinction applies to the residual closure.  Theorem 2.1
preserves `e_*` if it was already selected; inserting its lower colour as a
singleton does not create `e_*` when it was absent.

#### Proof

The source-word operation changes physical interval cells and their OR
values.  It does not alter the incidence graph, the endpoint usage of the
selected matchings, or the labelled-link graphic matroid.  These are exactly
the additional data in (3.2).  \(\square\)

Thus even after a prospective selector reduces `Cat_m` components to
`s=O(1)`, the final `s-1` component merges and the residual closure remain a
finite incidence/topology problem.  Split letters may pay the `O(s)` mask
casualties caused by chosen openings, but they do not choose the openings or
merge the components.

### Proposition 3.3 (literal finite paired-incidence collision)

The complete root-aligned, protected-disjoint pentagonal packet bank on the
three authenticated insured targets at `(m,h)=(4,1),(5,1),(5,2)` contains
`23` packets.  Exactly `18` admit a correlated second-matching reselection
with full upper palette, connector rank `Cat_m-1`, and the fixed
upper-transparent closure.  The other five fail before any scalar palette
test: two different lower rows force the same second-matching head.

In the unique `m=4` packet the protected row forces

\[
                         50\longmapsto54,
\]

while the new pentagonal row forces

\[
                         52\longmapsto54.                 \tag{3.3}
\]

Thus head injectivity is impossible even if the upper mask involved in
both rows is supplied elsewhere as an arbitrary interval OR.  This is the
smallest authenticated literal witness for Proposition 3.2 in the current
rooted-collar bank.

The independent replay is scoped only to these three finite targets; it is
not an all-`m` negative statement.  Its frozen identifiers are

```text
audit note SHA      6cb04d4c9408ff2f5e494bd70e199bbcfbf28e33f129e665beb344eb17546eed
search script SHA   cd5244d221890ce440b6bdc541c22ad729063ebc5c5d7ac2b86164a5e9692446
search JSON SHA     d35f719f69484bc3907ffe2cce720a30f95a76244b787c5272424c2fa26a7b1d
audit script SHA    aaf118c4b1bbd4402529b358f3cda5775204cb66b82216d6822773ad3f9cb8f5
audit JSON SHA      82324deb6f1e94947a9b1413c471d316e26446d9ab1dfe114e094406350eab2e
audit payload       b6a034b305f53f56d8d99bff90641e675a65b850c8bbd050dd1192a42ba7535d
```

## 4. Sharp monotone-pivot obstruction to creating a seam

One might try to evade Proposition 3.1 by using a genuinely new middle
window through a monotone inserted letter.  The exact complementary-join
formula shows why this is an additional hypothesis rather than a free
operation.

Insert `X` at a cut

\[
              \cdots,A_{-1}\mid A_1,\cdots,
              \qquad X\subseteq A_{-1}\cup A_1.          \tag{4.1}
\]

For compiler depth `h`, every internal new middle window has value

\[
                 O_i=\bigcup_{j=1}^{i}A_{-j}
                         \cup
                     \bigcup_{j=1}^{h-i}A_j,
                  \qquad1\le i<h.                        \tag{4.2}
\]

The inserted letter is redundant in (4.2).  Therefore a component-seam
pivot requires every `O_i` to be a legal rank-`m` owner, with the required
distinctness and chronology.

For the canonical shortest rotating-hole source

\[
                         A_j=K\cup\{z_j\},
              \qquad |K|=m-h-1,                          \tag{4.3}
\]

the `h` active labels in (4.2) are distinct, so

\[
                              |O_i|=m-1.                  \tag{4.4}
\]

No monotone split at that seam creates even one legal internal owner.  The
smallest case is `h=2`.  This is a literal one-seam obstruction, although it
does not rule out a noncanonical pivot-rich chronology or a nonmonotone
rethread.

## 5. Relation to the pentagonal orbit bank

The pentagonal packet cyclically reassigns three upper colours over the
same three lower colours.  A clean full rotation bank therefore changes no
outer palette.  Its proved role is physical graphic repair: in the frozen
`m=6,8` factors it removes the residual cycles and leaves exactly `Cat_m`
path components.

This separation is forced numerically.  In both the even central selector
and the odd rooted forest, the exact palette selector has

\[
                         |V|-|E|=\operatorname {Cat}_m.   \tag{5.1}
\]

A pentagonal `3<->3` move preserves `|E|`.  If its output is a forest, Euler
therefore forces exactly `Cat_m` components.  More generally `t` packets can
increase graphic rank by at most `3t`, so one rotation orbit of at most `2m`
packets pays at most `6m` connector-rank units.  This is exponentially
smaller than `Cat_m-O(1)`.

There is a second invariant after rooting.  Let `X,Y` be the unused tail and
head banks of a rooted partial matching and put

\[
                         g_i=d_i(Y)-d_i(X).               \tag{5.2}
\]

A residual incidence matching requires `g_i>=0` for every coordinate, and a
protected residual closure which adds coordinate `i` requires `g_i>=1`.
Every aligned pentagonal pivot leaves `X` fixed and replaces head holes
`{G,H}` by `{B,C}` with

\[
                    \chi(B)+\chi(C)=\chi(G)+\chi(H).      \tag{5.3}
\]

Hence it preserves every `g_i`.  Split letters act on source cells and also
leave this incidence budget unchanged.

The frozen `m=4` rooted Catalan forest makes this obstruction literal:

\[
                         g=(4,2,2,3,3,1,-1),              \tag{5.4}
\]

and residual matching rank is `11/14`.  It has one live
forest-preserving aligned pentagonal pivot; after that pivot the vector and
matching rank are still (5.4) and `11/14`.  Thus even an available packet
cannot repair a bad residual degree fibre.

Nothing in the orbit identity supplies the `Cat_m-1` matched connector links
of `Q_1`, and neither packet pivots nor split letters repair a negative
coordinate gap.  The exact all-dimensional gate is therefore still one of
the following:

1. an invariant selector which directly gives `Q_0` and all but `O(1)`
   connector links;
2. a rotation-bank absorber with a proved component-rank drop to `O(1)`
   together with a finite incidence completion; or
3. a noncanonical pivot-rich compiler which realizes the finite remaining
   seams and passes their paired incidence rows.

Only after one of these owner-layer statements is available does Theorem
2.1 turn bounded ordinary palette/compiler debt into bounded additive word
length.

The dimension-free rank/load theorem and its literal fixture are frozen in

```text
MATH_THEOREM_CATALAN_PENTAGONAL_ROOTED_PORT_PIVOT_AND_LOAD_OBSTRUCTION_20260801.md
  SHA 8f2cb1238284ff4e53e44f8ceab20b3e5d224b7e4c88cc850445392a6ddb2599
scratch/audit_catalan_pentagonal_rooted_port_pivot_20260801.py
  SHA 9a473954d6661eb610bfca447dd259e8c25ba610abda23c8697f0a86d5035023
scratch/catalan_pentagonal_rooted_port_pivot_20260801.audit.json
  SHA ca10637da5a69f52dd2436a69acf47295ef7249270747bca2fd32d5b7ec74253
  payload 04a5df5ece1eea46d4a5bd16f1ceadba9141bc60b8f1c226f697b28bd955b285
```

## 6. Scope audit

1. The positive theorem concerns literal OR-mask coverage and named
   contraction-stable witnesses.  It does not assert fixed-depth flatness;
   transported deadlines may increase by the number of inserted letters
   they cross.  A common-cap conclusion additionally needs the explicit cap
   and maximal-word clause in the definition before Theorem 2.1.
2. “Upper debt” in Theorem 2.1 means a missing upper mask in the final OR
   deck.  A missing paired occurrence in `Q_0` is excluded by Proposition
   3.2.
3. “Protected closure” means an already selected residual incidence edge
   and its named witnesses.  The theorem preserves but does not create it.
4. The component no-go is exact for the block-contraction architecture.  It
   is not an impossibility theorem for arbitrary rethreading.
5. The rank-`m-1` obstruction uses the canonical shortest-rail erosion.  It
   does not exclude a pivot-rich noncanonical source.
6. The theorem proves no all-`m` Catalan selector and no bound
   `nu(k)<=B(k)+O(1)` by itself.  It identifies the precise downstream role
   of the split-letter theorem once the connector gate is solved.
7. Proposition 3.3 is a complete packet census only for the three named
   insured `m=4,5` fixtures.  Its positive rows require correlated
   second-matching reselection; the raw pentagonal toggle alone is not
   claimed to preserve the rooted orientation.
8. The coordinate-gap obstruction (5.4) refutes universal post-hoc
   pentagonal completion of one rooted forest.  It does not refute choosing
   a different all-`m` forest in a degree-admissible fibre.

## 7. Finite replay of the universal rows

Run

```text
python3 scratch/audit_h1_split_letter_protected_catalan_finish_20260801.py
```

The replay exhausts every nonzero three-bit source word through length four,
every one-position dominated task, and every two-position dominated-task
pair on length-three words.  It separately exhausts one and two
adjacent-union cut insertions.  It checks injectivity and literal OR equality
for all transported intervals, component invariance for all graphs on at
most five vertices, and the canonical rank-`m-1` pivot row for every
`2<=h<=30`.  Its exact totals are

```text
one-bank block cases       29146
two-bank crossing cases     7581
one-cut pivot cases         39042
two-cut pivot cases          8695
labelled graph cases         1099
canonical pivot rows          435
```

The replay status is

```text
PASS_H1_SPLIT_LETTER_PROTECTED_CATALAN_FINISH
```

and the audit-script SHA-256 is

```text
ebe7a8dc7ebb679bc118172f6990e53d724a614340c6d71f8efca8b87b0629d8
```
