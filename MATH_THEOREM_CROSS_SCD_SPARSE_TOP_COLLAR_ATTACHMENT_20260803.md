# Cross-SCD sparse-top collar attachment by one exact Hall matching

**Date:** 2026-08-03  
**Status:** unconditional adjacent-slab Hall/matroid formulation and an
unconditional named-target cross-SCD construction.  No computation is used.
The theorem does not chainize the complete strict lower ideal and does not
assume Füredi's uniform-chain conjecture.

## 0. Outcome

Put

\[
                         n=2r,qquad
                         W={2r\choose r},qquad
                         p_s={{2r\choose s}\over W}.
\]

Fix a target depth `d`, a collar bottom rank `t<r`, and write

\[
                         a=r-t,qquad h=d-a.             \tag{0.1}
\]

Assume `h>=0`.  Let `B_1,...,B_q` be disjoint nonempty blocks of residual
ranks below `t`, put `s_j=max B_j`, and suppose

\[
              |B_j|\le h\quad(j\in[q]),
              \qquad
              \sum_{j=1}^q p_{s_j}\le p_t.             \tag{0.2}
\]

Then all named Boolean targets whose ranks lie in

\[
                         \left(\bigcup_j B_j\right)
                         \cup\{t,t+1,\ldots,r-1\}        \tag{0.3}
\]

can be partitioned into inclusion flags, assigned injectively to rank-`r`
owners, such that every flag has at most `d` targets.  Every target is used
at its literal set value and every flag is a prefix family of one ordering
of its assigned owner.

The residual chunks and collar chunks may come from two unrelated symmetric
chain decompositions.  Their only coupling is one exact containment
matching.  Thus this is a genuine cross-SCD rechainization theorem.

A concrete special case is obtained from one adjacent lower slab

\[
                         B_1=\{t-h,\ldots,t-1\}.         \tag{0.4}
\]

Since `p_(t-1)<=p_t`, condition (0.2) holds.  Hence every named target in
the complete central band

\[
                         t-h\le |S|\le r-1              \tag{0.5}
\]

fits exactly into owner flags of length at most `a+h=d`.  With
`t=r-a` and `h=d-a`, this is the full `d`-rank band
`r-d,...,r-1`.

The theorem is a sufficient slab case, not the missing complete-ideal
theorem.  Section 5 compares its density condition with the uniform-chain
frontier.

## 1. Exact adjacent-slab Hall formulation

The following statement is independent of symmetric chain decompositions.

Let `mathcal R` be a family of pairwise target-disjoint residual flags.  For
`F in mathcal R`, write `top(F)` for its maximum and `ell(F)=|F|`.

Let `mathcal C` be a family of pairwise target-disjoint collar flags.  Every
`D in mathcal C` has a minimum `bot(D)`, a maximum `top(D)`, a load
`ell(D)`, and a distinct assigned owner `T_D` satisfying

\[
                         \operatorname{top}(D)\subset T_D. \tag{1.1}
\]

Make the attachment graph `Gamma` from `mathcal R` to `mathcal C` by

\[
 F\sim D
 \quad\Longleftrightarrow\quad
 \operatorname{top}(F)\subset\operatorname{bot}(D)
 \quad\hbox{and}\quad
 \ell(F)+\ell(D)\le d.                                 \tag{1.2}
\]

### Theorem 1.1 (two-slab attachment criterion)

Every residual flag can be attached to a different collar flag, producing
owner flags of load at most `d`, if and only if

\[
                         |N_\Gamma(X)|\ge|X|
                    \qquad(X\subseteq\mathcal R).       \tag{1.3}
\]

The attachable residual subfamilies form the transversal matroid of
`Gamma`, with rank

\[
 r_\Gamma(Y)=
 \min_{X\subseteq Y}
 \bigl(|Y\setminus X|+|N_\Gamma(X)|\bigr).              \tag{1.4}
\]

### Proof

Condition (1.3) is Hall's theorem for a matching saturating `mathcal R`.
For a matched pair `(F,D)`, every member of `F` lies below `top(F)`, which
lies below `bot(D)`, so `F union D` is one inclusion flag.  Equation (1.2)
gives its load bound, and (1.1) places the combined flag inside `T_D`.
Unmatched collar flags remain unchanged.  Distinct matched collar flags
have distinct owners, so owner capacity is preserved.

Conversely, any attachment using each collar flag at most once gives a
matching saturating `mathcal R`, so Hall is necessary.  Formula (1.4) is
the standard rank formula for the transversal matroid. \(\square\)

Theorem 1.1 is the exact adjacent-slab formulation.  It is matroidal after
the owner-rooted collar bank has been fixed.  Selecting the collar bank,
its owners, and the residual attachments simultaneously is a stronger
three-resource problem and is not claimed to be a matroid.

## 2. Two independent SCDs

Fix arbitrary symmetric chain decompositions

\[
                         \mathscr S_R,\qquad \mathscr S_C
\]

of `B_(2r)`.  They need not agree.

### Residual chunks

For `C in mathscr S_R` and a rank block `B_j`, put

\[
                         C[B_j]=\{X\in C:|X|\in B_j\},  \tag{2.1}
\]

discarding empty chunks.  Since an SCD chain is saturated and `s_j<r`, a
nonempty chunk contains the unique rank-`s_j` set of its chain, and that set
is its top.  Consequently the chunks with block label `j` are canonically
indexed by the complete layer

\[
                              { [2r]\choose s_j}.        \tag{2.2}
\]

Every residual chunk has at most `|B_j|<=h` members.

### Collar chunks and sockets

For `D in mathscr S_C`, put

\[
                         D[t,r-1]=\{X\in D:t\le|X|\le r-1\},
                                                                  \tag{2.3}
\]

again discarding empty chunks.  Every nonempty collar chunk ends at its
unique rank-`r-1` member.  Hence all collar chunks are canonically indexed
by the complete rank-`r-1` layer.

Those collar chains which meet rank `t` have bottom equal to their unique
rank-`t` member and contain exactly one target at every rank
`t,...,r-1`.  Call them the **socket chunks**.  They are canonically indexed
by the complete layer

\[
                              { [2r]\choose t},          \tag{2.4}
\]

and every socket chunk has load exactly `a=r-t`.  Collar chunks whose SCD
chain starts above `t` have smaller load and need no residual attachment.

## 3. Uniform containment flow closes every socket Hall cut

Make a bipartite graph from all residual chunks to all rank-`t` socket
chunks.  A residual chunk with top `S` is adjacent to the socket with
bottom `T` exactly when

\[
                              S\subset T.               \tag{3.1}
\]

### Lemma 3.1 (sparse-top socket matching)

Under (0.2), this graph has a matching saturating every residual chunk.

### Proof

A rank-`s` top lies in

\[
                              {2r-s\choose t-s}          \tag{3.2}
\]

rank-`t` sets.  Send its chunk uniformly to those sockets.  Every residual
chunk has total outgoing weight one.

A fixed rank-`t` socket contains `binom(t,s)` possible rank-`s` tops from
block `j`.  Its incoming load from that block is

\[
 { {t\choose s}\over {2r-s\choose t-s}}
 ={ {2r\choose s}\over {2r\choose t}}
 ={p_s\over p_t}.                                      \tag{3.3}
\]

Summing over the blocks gives total socket load

\[
                              {1\over p_t}\sum_jp_{s_j}\le1.
                                                                  \tag{3.4}
\]

Thus we have a fractional matching saturating every residual chunk and
respecting unit socket capacities.  The bipartite matching polytope is
integral, so an integral saturating matching exists. \(\square\)

This argument proves all subset Hall inequalities simultaneously; no
independence or randomness between named chunks is assumed.

## 4. Named cross-SCD flag theorem

### Theorem 4.1

Under (0.1)--(0.2), the conclusion in Section 0 holds.

### Proof

Use Lemma 3.1 to attach every residual chunk to a different socket chunk.
The residual top is strictly contained in the rank-`t` socket bottom.  The
concatenation is therefore an inclusion flag.  Its load is at most

\[
                              h+a=d.                    \tag{4.1}
\]

Every residual target in the selected rank blocks occurs in exactly one
chunk of `mathscr S_R`; every collar target occurs in exactly one chunk of
`mathscr S_C`.  Hence the resulting flags partition the named target family
in (0.3) exactly.

It remains to assign owners.  Every resulting flag ends at a distinct
rank-`r-1` set, namely the top of its collar chunk.  The containment graph
between ranks `r-1` and `r` is biregular, with left degree `r+1` and right
degree `r`.  Therefore, for every family `X` of rank-`r-1` sets,

\[
                         (r+1)|X|\le r|N(X)|,
\]

so Hall matches all rank-`r-1` tops to distinct rank-`r` owners.  Every set
in the corresponding combined flag lies below its top and hence inside its
owner.

Finally, any finite strict inclusion flag inside an owner extends to the
prefixes of an ordering of that owner: list successive set differences and
then the unused owner elements.  This proves all claims. \(\square\)

### Corollary 4.2 (complete adjacent band)

Let `1<=h<=d-a` and `t-h>=1`.  Taking the single block

\[
                              B=\{t-h,\ldots,t-1\}
\]

satisfies (0.2), because its top is `t-1` and
`p_(t-1)<=p_t` below the middle rank.  Hence every named target of ranks
`t-h,...,r-1` has an exact owner-flag realization of maximum load `a+h`.

In particular, if `h=d-a`, every target in the `d` consecutive lower
central ranks `r-d,...,r-1` is realized in flags of load at most `d`.
When `h=0`, the collar-only assertion is immediate and needs no residual
block.

### Corollary 4.3 (boundary deletion and sparse residual families)

After Theorem 4.1, delete any prescribed named targets from any selected
rank.  The retained flags remain nested and owner-disjoint, and their loads
only decrease.  If every residual block has no adjacent ranks, the retained
residual portion of every flag has the same nonadjacency property.

## 5. Relation to the antitone theorem and the Füredi frontier

The antitone residual--collar theorem proves that the anonymous rank
inventory always fits at optimal depth `d`: balance the two row-load vectors
and couple them in opposite order.  The present theorem supplies a named
integral lift on the sparse-top face (0.2).  The price for naming is visible
and exact: one rank-`t` socket can accept only one residual SCD chunk, so the
total density of residual chunk tops must not exceed `p_t` in the uniform
containment proof.

This does not prove the complete named-flag theorem.  In the known
sparse-top residual construction, the total top density is below one, but
need not be below the single-socket density `p_t`.  Closing the whole ideal
may require:

* sockets at several collar depths with their different residual
  capacities;
* serial cross-chain splices which place more than one compatible residual
  chunk below one collar flag; or
* a joint collar decomposition chosen in response to the residual chunks.

Those operations are outside the one-matching theorem above.

Nor does Theorem 4.1 imply Füredi's floor/ceiling uniform-chain conjecture.
It chainizes only the selected residual rank blocks plus one lower collar,
may leave all other lower ranks unused, and controls only a maximum flag
length.  It does not partition the full Boolean lattice into width-many
floor/ceiling chains, impose rank symmetry, or balance every chain size.

Conversely, taking enough rank blocks to cover the complete strict lower
ideal is not justified by (0.2).  The audited single-SCD barrier shows that
merely chopping one fixed SCD into depth-`d` pieces requires more than `W`
flags by a positive linear fraction.  Thus the remaining complete-ideal
theorem still lies on the genuine cross-chain/equitable-chain frontier.

The proof-safe gain is narrower but exact:

\[
 \boxed{
 \sum_jp_{s_j}\le p_t,quad |B_j|\le d-(r-t)
 \ \Longrightarrow\
 \text{exact named residual--collar flags at depth }d.}
\]
