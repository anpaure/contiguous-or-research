# K16 `c279 -> 2c6d` facet-colour augmentation

## 1. Exact verdict and scope

The authenticated literal source is

```text
scratch/k16_upper12874_best_delete.word
SHA a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

of length 12,873.  For each left endpoint, stop at the first interval OR of
rank at least eight.  Every start gives a rank-eight target.  The resulting
occurrence path contains every rank-eight label except

```text
H = 2c6d
```

and contains four labels twice: the three same-deadline flats `4e71`,
`cc63`, `ce61`, and the different-deadline duplicate

```text
D = c279.
```

The two occurrences of $D$ are at starts 11,726 and 12,826, with deadlines
11,728 and 12,828.  Their incident rank-nine colours are respectively

```text
c379, e279       and       ca79, c679.
```

This note proves a positive result at the occurrence-labelled carrier level:
an optimal pair of four-step facet-colour augmenting paths deletes the second
copy of $D$, installs $H$, preserves every rank-nine edge-colour token
exactly, and leaves one connected Hamilton path on the occurrence nodes.

It does **not** yet lift that path to one literal overlapping-interval word or
to the frozen pass33 lower matching.  Thus it is an exact carrier theorem,
not a K16 word or Hall improvement.

## 2. Endpoint-incidence normal form

Let $V$ be the rank-eight masks and let ${\cal E}$ be occurrence-labelled
edge tokens.  Token $e$ has a fixed rank-nine colour $U_e$.  A realization
chooses two distinct facets of $U_e$ as the endpoints of $e$.

For a colour $U$, let $\mu_U$ be the number of tokens of colour $U$, and let
$z_{XU}$ be the number of their endpoint incidences at facet $X\subset U$.
Let $b_X$ be the total required degree of occurrences carrying label $X$;
for a 2-factor $b_X=2m_X$, while a path subtracts one at each fixed endpoint
label.

### Theorem 2.1 (abstract colour-factor criterion)

A prescribed label multiplicity and fixed colour-token multiset have a
loopless abstract realization if and only if there are integers $z_{XU}$
satisfying

\[
 z_{XU}\ge0,\qquad z_{XU}=0\quad(X\not\subset U),                 \tag{2.1}
\]

\[
 \sum_{X\subset U}z_{XU}=2\mu_U,qquad
 \max_{X\subset U}z_{XU}\le\mu_U,                              \tag{2.2}
\]

and

\[
 \sum_{U\supset X}z_{XU}=b_X.                                  \tag{2.3}
\]

For a connected path or cycle, connectivity of the resulting occurrence
pairing is an additional condition.

#### Proof

Necessity is immediate.  For fixed $U$, (2.2) is precisely the criterion for
pairing the $2\mu_U$ endpoint tokens into $\mu_U$ pairs with unequal facet
labels: the largest class must fit against all other classes.  Sufficiency
follows by such a pairing independently for every $U$, producing loopless
coloured edges.  Equation (2.3) then supplies exactly the required number of
half-edges at every label; partition those half-edges among its prescribed
degree-one or degree-two occurrence nodes.  This realizes the degree and
colour data.  The construction need not connect the components, which is why
connectivity is separate. QED.

The theorem is an exact small integer-flow formulation of the abstract
carrier gate.  It does not encode physical interval chronology.

## 3. Alternating facet-colour paths

Write

\[
 X\xrightarrow[e:U]{Z}Y
\]

when token $e$ currently joins $X$ to the fixed mate $Z$, has colour $U$, and
we replace endpoint $X$ by a different facet $Y\subset U$ while retaining
$Z$.  Necessarily $Y\cup Z=U$.

### Theorem 3.1 (two-path decomposition)

Restrict to switches which change at most one endpoint of each edge token.
Deleting one internal occurrence of $D$ and inserting one internal occurrence
of $H$ is possible exactly when the signed endpoint changes decompose into

1. two token-disjoint directed facet-colour paths from $D$ to $H$, starting
   with the two edge tokens incident with the deleted $D$ occurrence; and
2. any number of neutral directed cycles.

Under unit internal-occurrence capacity the two paths may be chosen
internally occurrence-disjoint.  Flipping their endpoint incidences preserves
every colour-token count and every internal degree.

#### Proof

Orient every changed endpoint incidence from its old facet to its new facet.
Every edge token contributes at most one directed step.  Colour degree is
unchanged by construction.  At every retained vertex occurrence, old and new
degree agree, so indegree equals outdegree in the change digraph.  The deleted
$D$ occurrence contributes two excess outgoing units and the inserted $H$
occurrence two excess incoming units.  Integral flow decomposition therefore
gives two $D$--$H$ paths and cycles.  The first tokens must be the two tokens
formerly incident with the deleted occurrence.  Conversely, flipping any
such paths and cycles gives exactly these degree changes. QED.

In particular, one augmenting path can never suffice: the missing occurrence
requires two endpoint units.

## 4. Sharp endpoint lower bound

The Johnson distance between $D$ and $H$ is

\[
 d_J(D,H)=\frac{|D\mathbin\triangle H|}{2}=4.                    \tag{4.1}
\]

Every facet-colour step is one Johnson edge, so every $D$--$H$ path has
length at least four.  For the second $D$ copy, colours `ca79` and `c679`
add respectively bits `0800` and `0400`, both belonging to $H\setminus D$.
Thus two length-four paths, eight changed tokens total, are the absolute
minimum.

For the first copy, `c379` adds `0100`, which is not in $H\setminus D$;
that path has length at least five, while the `e279` path has length at least
four.  Hence deleting the first copy costs at least nine tokens in this
one-endpoint-per-token model.

## 5. Explicit optimal augmentation

Index the original occurrence targets by $v_0,\ldots,v_{12872}$ and let edge
token $e_i$ join $v_i$ to $v_{i+1}$.  The following two paths start with the
two tokens incident with the second $D$ occurrence.

First path:

```text
c279 -- e12825:ca79, mate ca71 --> ca69
ca69 -- e9534 :ea69, mate ea68 --> aa69
aa69 -- e9956 :aa6d, mate aa65 --> a86d
a86d -- e6438 :ac6d, mate a46d --> 2c6d
```

Second path:

```text
c279 -- e12826:c679, mate c639 --> c669
c669 -- e10033:e669, mate e661 --> a669
a669 -- e10924:ae69, mate ac69 --> 2e69
2e69 -- e4486 :2e6d, mate 266d --> 2c6d
```

The eight edge tokens are distinct and the six internal facets are distinct.
For each line, the new endpoint and fixed mate are distinct rank-eight facets
whose union is the displayed rank-nine colour.

### Theorem 5.1 (optimal abstract Hamilton augmentation)

Flip the eight endpoint incidences above, delete occurrence 12,826 of
`c279`, and add one occurrence of `2c6d`.  Then:

1. every occurrence node has degree two except the two unchanged path
   endpoints, which have degree one;
2. the occurrence graph is connected, hence is one Hamilton path on 12,873
   nodes;
3. every rank-eight target is present, with only the three old flat labels
   `4e71`, `cc63`, `ce61` repeated;
4. the colour of every individual edge token is unchanged.

The support of eight tokens is optimal under Theorem 3.1.

#### Proof

Along each path, every internal occurrence gains the preceding endpoint and
loses the following endpoint.  The deleted $D$ copy loses its two incident
tokens and the new $H$ occurrence gains the two terminal tokens.  This proves
the degree and label statements.  Direct traversal from the unchanged first
endpoint visits all 12,873 occurrence nodes exactly once and ends at the
unchanged last endpoint.  The facet-union identity on every line proves
tokenwise colour equality.  Optimality is Section 4. QED.

The literal source has 12,867 stored rank-nine edge occurrences covering all
11,440 rank-nine colours, so its strict stored-edge surplus is 1,427.  The
frequently used 1,430 normalization adds three connector slots.  The theorem
does not depend on either convention because it preserves the complete
stored colour-token multiset rather than spending a surplus colour.

## 6. Exact physical and matching gate

The augmentation solves only the coloured degree quotient.  A physical lift
must produce one literal word whose overlapping intervals induce the new
occurrence path.  It must additionally retain all deeper upper masks and
satisfy the first-middle equality ledger.  Target adjacency alone does not
imply this overlap realization.

Nor is the frozen pass33 matching automatically available here.  It belongs
to a different authenticated middle chronology and maximal-envelope word.
To combine the two lanes, each lifted endpoint atom must carry the signature

\[
 \Pi=(e,U,X,Z,Y;\ \text{boundary envelopes};\
       \Delta(G,S,J,F);\ \mathbf 1_{2c6d},\mathbf 1_{c679};\
       \text{exterior-loss bitset};\ \text{residual adjacency}).             \tag{6.1}
\]

Atoms compose only when occurrence flow and boundary states close.  After an
explicit map into pass33, retaining every exterior edge reduces the protected
Hall test to the already-proved 75-left residual matching threshold 52.  In
the absence of that map, applying the pass33 oracle here would be circular.

Thus the smallest exact remaining lemma is:

> **Eight-token chronology-lift gate.**  Lift the two paths in Section 5 (or
> another token-disjoint optimal pair) to dependency-compatible literal
> packets which preserve the named pair, arbitrary upper coverage, and the
> exterior pass33 matching, and whose 75-left residual graph has matching at
> least 52.

This is narrower than a generic global braid and strictly broader than the
closed width-at-most-four one-token packet classes.

## 7. Frozen audit

```text
scratch/audit_threadA_k16_c279_h_facet_color_augmentation_20260731.py
  SHA 2c2f15d6fa20a263ca56ee7ff223d1f6938ccdb299d26bc644e93696f0629cd2
scratch/threadA_k16_c279_h_facet_color_augmentation_20260731.audit.json
  SHA a625ca004c093e1ee56cb371eaadcbc4f403eb25e2df563fdfdc9b25b9cecbed
  payload 2ddf515ff95fc5a7eea6eada3f7c7fea766ed8d6d4d3fb02621b863c71beea3c
```

The audit independently reconstructs the first-middle occurrence deck,
checks all eight facet replacements token by token, compares the complete old
and new colour-token lists, and traverses the new occurrence graph.  It is a
light deterministic replay; no SAT solver or exhaustive local search is
used.
