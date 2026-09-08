# Odd-distance residence: the `k=9` certificate and the `k=21` prediction

Date: 2026-07-28

Status: theorem plus exact audit of the normalized `k=9,11,13` words.  No
`k=21` construction is claimed.

## 1. The theorem

Let a Johnson chronology have transitions

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\]

Interleave the transition labels as

\[
 z_{2i}=b_i,\qquad z_{2i+1}=a_{i+1}.
\]

Then depth-`d` residence is exactly

\[
 b_i\ne a_{i+t}\qquad(1\le t\le d),
\]

or, in the interleaved word,

\[
 \boxed{z_{2i}\ne z_{2i+2t-1}
        \qquad(1\le t\le d).}
 \tag{1.1}
\]

For an antipodal odd-graph lift the distance-one case is automatic, so the
nontrivial forbidden odd distances are

\[
                         3,5,\ldots,2d-1.
 \tag{1.2}
\]

This law depends on the optimal depth `d(k)`, not on the proper divisors of
`k`.

## 2. Exact certificate audit

The normalized source words in `answers/` give the following counts.  A
"bad" occurrence at distance `2t-1` means `b_i=a_(i+t)` within the linear
middle chronology.

\[
\begin{array}{c|c|rrrr}
k&d&1&3&5&7\\ \hline
9 &2&0&0&40&-\\
11&3&0&0&0&142\\
13&3&0&0&0&429
\end{array}
\]

Thus `k=9` has exactly the predicted single *nonautomatic* exclusion at
distance three, and the next distance already fails 40 times.  Likewise the
`k=11` and `k=13` words exclude exactly the required distances through five
and acquire many collisions at seven.  The threshold is sharp in all three
certificates.

## 3. Consequence for `k=21`

The lower-bound arithmetic gives

\[
 r=11,\qquad W=\binom{21}{11}=352716,qquad d(21)=3,
 \qquad B(21)=352719.
\]

Therefore the residence theorem predicts nontrivial exclusions at distances

\[
                              3\quad\text{and}\quad5,
\]

not at `3` and `7`.  A distance-seven exclusion may arise from a particular
`Z_21`-equivariant ansatz, but it is not required by residence or optimal
length.

There is a genuine divisor phenomenon elsewhere: translation-invariant
excess designs decompose into orbit sizes indexed by divisors of `k` (the
forced size-five orbit at `k=15` is the first example).  The certificate
audit separates the two effects:

* odd memory distances `3,5,...,2d-1` come from residence;
* short orbit sizes come from the factorization of `k`.

They coincide accidentally at `k=15`, where `d=3` and the nontrivial memory
distances `3,5` are also the prime divisors of `15`.  The `k=21` case is the
first clean discriminator.

